from django.urls import path
from . import views

urlpatterns = [
        path("", views.postcontent, name = 'content'),
        path("details/<int:pk>", views.details_page, name = "details"),
        ]