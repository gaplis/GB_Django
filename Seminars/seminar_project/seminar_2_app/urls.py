from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('last/', views.last_games, name='last_games'),
    path('authors/', views.author, name='authors'),
]