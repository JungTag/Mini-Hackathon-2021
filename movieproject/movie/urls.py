from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('detail/<int:id>', views.detail, name="detail"),
    path('comment/create/<int:id>', views.comment_create, name="comment_create"),
]
