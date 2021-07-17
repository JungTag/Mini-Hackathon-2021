from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie

import requests

# Create your views here.
def init_db(request):
    url = "http://3.36.240.145:3479/mutsa"
    res = requests.get(url)
    datas = res.json()['movies']
    
    for d in datas:
        movie = Movie()
        movie.title_kor = d['title_kor']
        movie.title_eng = d['title_eng']
        movie.postr_url = d['postr_url']
        movie.rating_aud = d['rating_aud']
        movie.rating_cri = d['rating_cri']
        movie.rating_net = d['rating_net']
        movie.genre = d['genre']
        movie.showtimes = d['showtimes']
        movie.release_date = d['release_date']
        movie.rate = d['rate']
        movie.summary = d['summary']
        # movie.staff = d.staff -> 객체로
        movie.save()
        print(movie)
    return redirect('index')

def index(request):
    movies = Movie.objects.order_by('title_kor')
    return render(request, 'index.html', {'movies': movies})

def detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'detail.html', {'movie': movie})