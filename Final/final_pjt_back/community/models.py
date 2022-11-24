from django.db import models
from django.conf import settings
from movies.models import Movie


# yt code
class Review(models.Model):
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


# class Comment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
#     review = models.ForeignKey(Review, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
# class Review(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
#     # funny_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='funny_reviews')
#     # helpful_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='helpful_reviews')
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
#     title = models.CharField(max_length=100)
#     liked = models.BooleanField()
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)