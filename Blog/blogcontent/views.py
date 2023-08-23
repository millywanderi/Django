from django.shortcuts import render, redirect
from .models import Blog, Comment
from .models import Category
from .forms import CommentForm

def postcontent(request):

    posts = Blog.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "postcontent.html", context)

def details_page(request, pk):
    post = Blog.objects.get(pk = pk)
    comments = Comment.objects.filter(post_comment = pk)
    context = {
        "post": post,
        "comments": comments,
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