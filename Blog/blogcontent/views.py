from django.shortcuts import render
from .models import Blog
from .models import Category

def postcontent(request):

    posts = Blog.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "postcontent.html", context)

def details_page(request, pk):
    post = Blog.objects.get(pk = pk)
    context = {
        "post": post,
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