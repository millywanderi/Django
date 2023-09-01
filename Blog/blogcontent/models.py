from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Category(models.Model):
    category = models.CharField(default="coding",max_length = 100)

    def __str__(self):
        return f'{self.category}'

class Blog(models.Model):
    post = models.TextField()
    title = models.CharField(max_length=100)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_post = models.DateField(default=date.today)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to="images")
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-date_of_post", ) # order to be the lastest

    def __str__(self):
        return f'{self.title} {self.date_of_post}'

    @property
    def total_likes(self):   
        likes = Like.objects.filter(post=self, liked=True)
        total = 0
        if likes:
            for like in likes:
                total += like.likes
        return total

class Like(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    likes = models.IntegerField(default=0)
    liked = models.BooleanField(default=False)

    varbose_name_plural = "Likes"

    def __str__(self):
        return f'total likes for {self.post.title} {self.likes}'

class Comment(models.Model):
    comment = models.TextField(max_length = 200)
    date_of_comment = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    post_comment = models.ForeignKey(Blog, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.post_comment}'
    
class Review(models.Model):
    post_review = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_of_review = models.DateField(auto_now_add = True)
    review = models.TextField(max_length=300)

    def __str__(self):
        return f'Review for {self.post_review} by {self.user.username}'
