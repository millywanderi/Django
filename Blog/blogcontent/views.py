from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment, Review, Like
from .models import Category
from .forms import CommentForm, EditPostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def postcontent(request):

    posts = Blog.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "postcontent.html", context)

def details_page(request, pk):
    post = Blog.objects.get(pk = pk)
    comments = Comment.objects.filter(post_comment = pk)
    likes = post.total_likes
    print()
    print(likes)
    context = {
        "post": post,
        "comments": comments,
        "likes" : likes,
    }
    return render(request, "details_page.html", context)

def all_categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'category.html', context)

def each_category(request, category):
    posts = Blog.objects.filter(category__category = category)

    context = {
        "posts": posts,
        "cat": category,
    }
    return render(request, "each_category.html", context)

def comment(request, pk):
    post = Blog.objects.get(pk = pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            user = request.user
            post_comment = post

            comment = Comment.objects.create(comment = comment,
                                             user = user,
                                             post_comment = post_comment
                                             )
            comment.save()

        else:
            print(form.errors)
    return redirect("details", pk)

def review(request, pk):
    
    post_review = Blog.objects.get(pk=pk)
    all_reviews = Review.objects.filter(post_review = post_review)

    if request.method == "POST":
        userReview = request.POST.get("review", "")
        if userReview:
            reviews = Review.objects.filter(user=request.user, post_review=post_review)

            if reviews.count() > 0:
                first_review = reviews.first()
                first_review.review = userReview
                first_review.save()
            else:
                first_review = Review.objects.create(
                    post_review = post_review,
                    user = request.user,
                    review = userReview
                ) 
        return redirect("review", pk=post_review.pk)
    context = {
        "post_review" : post_review,
        "user" : request.user,
        "all_reviews" : all_reviews,
                }
    return render(request, "review.html", context)

def postLike(request, pk):
    
    post = get_object_or_404(Blog, pk=pk)
    like, created = Like.objects.get_or_create(post = post,
                                               user = request.user
                                               )
    if created or not like.liked:
        like.liked = True
        like.likes = 1
    else:
        like.liked = False
        like.likes = 0

    like.save()

    return HttpResponseRedirect(reverse("details", args=(post.pk,)))

def editPost(request, pk):

    post = Blog.objects.get(pk=pk)
    if request.method == "POST":
        editForm = EditPostForm(request.POST, request.FILES, instance=post)
        if editForm.is_valid():
            editForm.save()
            messages.success(request, f'Your changes have been saved')
            return redirect("editpost", pk=pk)
    else:
        editForm = EditPostForm(instance=post)
    context = {
        'editForm' : editForm,
        'post' : post
    }

    return render(request, "editPost.html", context)
