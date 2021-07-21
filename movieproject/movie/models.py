from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    title_kor = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    poster_url = models.CharField(max_length=255, null=True)
    rating_aud = models.CharField(max_length=10)
    rating_cri = models.CharField(max_length=10)
    rating_net = models.CharField(max_length=10)
    rating_rut = models.FloatField(default=0) # 루튼 토마토 평점
    total_cnt = models.IntegerField(default=0) # 평가자 수
    genre = models.CharField(max_length=100)
    showtimes = models.CharField(max_length=10)
    release_date = models.CharField(max_length=20)
    rate = models.CharField(max_length=100)
    summary = models.TextField()


class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Staff(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    image_url = models.CharField(max_length=255, null=True)
