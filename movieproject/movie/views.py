from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Staff
from .pagination_range import get_pagination_range
from django.core.paginator import Paginator

import requests

# Create your views here.
def init_db(request):
    url = "http://3.36.240.145:3479/mutsa"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        new_movie = Movie()
        new_movie.title_kor = movie['title_kor']
        new_movie.title_eng = movie['title_eng']
        new_movie.poster_url = movie['poster_url']
        new_movie.rating_aud = movie['rating_aud']
        new_movie.rating_cri = movie['rating_cri']
        new_movie.rating_net = movie['rating_net']
        new_movie.genre = movie['genre']
        new_movie.showtimes = movie['showtimes']
        new_movie.release_date = movie['release_date']
        new_movie.rate = movie['rate']
        new_movie.summary = movie['summary']
        new_movie.save()
        staffs = movie['staff']
        for staff in staffs:
            new_staff = Staff()
            new_staff.movie = new_movie
            new_staff.name = staff['name']
            new_staff.role = staff['role']
            new_staff.image_url = staff['image_url']
            new_staff.save()
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
    staffs = Staff.objects.filter(movie = movie)
    return render(request, 'detail.html', {'movie': movie, 'staffs': staffs})