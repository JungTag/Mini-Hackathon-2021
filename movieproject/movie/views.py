from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .pagination_range import get_pagination_range
from django.core.paginator import Paginator

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
    if 'query' in request.GET:
        query = request.GET['query']
        movies = Movie.objects.filter(
            title_kor__contains=query
        ).order_by('title_kor')
    else:
        query = None
        movies = Movie.objects.all().order_by('title_kor')
    
    paginator = Paginator(movies, 8)
    page = request.GET.get('page', 1)
    paginated_movies = paginator.get_page(page)
    current_page = int(page) if page else 1
    max_index = len(paginator.page_range)
    start_index, end_index = get_pagination_range(current_page, max_index)
    page_num_range = paginator.page_range[start_index:end_index]
    
    if query:
        return render(request, 'index.html', {'movies': paginated_movies, 'page_range': page_num_range, 'query': query})
    else:
        return render(request, 'index.html', {'movies': paginated_movies, 'page_range': page_num_range})

def detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'detail.html', {'movie': movie})