from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title_kor = models.CharField(max_length=200)
    title_eng = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="poster/", blank=True, null=True)
    rating_aud = models.FloatField(null=True)
    rating_cri = models.FloatField(null=True)
    rating_net = models.FloatField(null=True)
    genre = models.CharField(max_length=100)
    showtimes = models.IntegerField(null=True)
    release_date = models.IntegerField(null=True)
    rate = models.CharField(max_length=200)
    summary = models.TextField()
    staff = models.CharField(max_length=200)

class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="movie", on_delete=models.CASCADE)