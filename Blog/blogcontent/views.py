from django.shortcuts import render
from .models import Blog

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