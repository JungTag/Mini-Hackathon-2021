from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title_kor = models.CharField(max_length=200)
    title_eng = models.CharField(max_length=200)
    postr_url = models.CharField(max_length=200, null=True)
    rating_aud = models.CharField(max_length=10)
    rating_cri = models.CharField(max_length=10)
    rating_net = models.CharField(max_length=10)
    genre = models.CharField(max_length=100)
    showtimes = models.CharField(max_length=10)
    release_date = models.CharField(max_length=20)
    rate = models.CharField(max_length=200)
    summary = models.TextField()
    staff = models.CharField(max_length=200)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)