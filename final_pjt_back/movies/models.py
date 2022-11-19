from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    #pk = models.IntegerField()
    name = models.CharField(max_length=50)

    #def __str__(self) : # admin 페이지에서 편하게 보기 위함
    #    return self.name

class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    #pk = models.IntegerField()
    name= models.CharField(max_length=50)
    profile_path = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'

class Keyword(models.Model):
    keyword_id = models.IntegerField(primary_key=True)
    #pk = models.IntegerField()
    name = models.CharField(max_length=100)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    # pk = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    # actor_ids = models.IntegerField()
    actor_ids = models.ManyToManyField(Actor)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=200)
    video_path = models.CharField(max_length=200)
    # keywords = models.IntegerField()
    keywords = models.ManyToManyField(Keyword)

    #def __str__(self) :
    #    return self.title
    
#class Actor(models.Model) :


    #def __str__(self) : # admin 페이지에서 편하게 보기 위함
    #    return self.name


# class Tournament(models.Model) :
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tournaments')
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
