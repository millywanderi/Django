from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Blog(models.Model):
    post = models.TextField()
    title = models.CharField(max_length=100)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_post = models.DateField(default=date.today)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return f'{self.title} {self.date_of_post}'
