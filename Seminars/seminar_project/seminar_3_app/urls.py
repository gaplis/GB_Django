from django.urls import path
from .views import HomeViews, AboutViews, OrelViews, CubeViews, RandomViews, AllAuthorPostsViews, PostViews

urlpatterns = [
    path('home/', HomeViews.as_view(), name='home'),
    path('about/', AboutViews.as_view(), name='about'),
    path('orel/<int:count>/', OrelViews.as_view(), name='orel'),
    path('cube/<int:count>/', CubeViews.as_view(), name='cube'),
    path('random/<int:count>/', RandomViews.as_view(), name='random'),
    path('author/<int:id_author>/', AllAuthorPostsViews.as_view(), name='author'),
    path('post/<int:pk>/', PostViews.as_view(), name='post'),
]