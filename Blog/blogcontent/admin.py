from django.contrib import admin
from .models import Blog, Category, Comment, Review, Like
# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Like)