from django.db import models
from django.conf import settings
# from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=300)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Keyword(models.Model):
    name = models.CharField(max_length=100)

# class Movie(models.Model):
#     title = models.CharField(max_length=200)
#     poster_path = models.CharField(max_length=100)
#     popularity = models.IntegerField()
#     vote_average = models.FloatField()
#     release_date = models.CharField(max_length=100)
#     overview = models.TextField()
#     genre_ids = models.ManyToManyField(Genre)
#     actor_ids = models.ManyToManyField(Actor)
#     director_id = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movies")
#     user_watched = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watched_movie')
#     user_wished = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="wish_movie")


class Movie(models.Model):
    title = models.CharField(max_length=50)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")
    keywords = models.ManyToManyField(Keyword, related_name="movies")
    release_date = models.DateField()
    # wish_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="wish_movie")
    poster_path = models.CharField(max_length=200)
    video_path = models.CharField(max_length=200)


#class Review(models.Model):
#    title = models.CharField(max_length=20)
#    content = models.CharField(max_length=200)
#    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
#    reviewed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")


#class WatchedMovie(models.Model):
#    rate = models.FloatField(
#        default=0,
#        validators=[
#            MaxValueValidator(5),
#            MinValueValidator(0.5)
#        ]
#    )
#    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="watched_movie")
#    watched_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="watched_movie")


# class Review(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="review")
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")
#     title = models.CharField(max_length=50)
#     content = models.TextField()
#     rate = models.FloatField(
#         default=0,
#         validators=[
#             MaxValueValidator(5),
#             MinValueValidator(0.5)
#         ]
#     )
