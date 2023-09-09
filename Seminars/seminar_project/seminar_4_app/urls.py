from django.urls import path
from .views import game_view, AddAuthor, AuthorPage, AddPost

urlpatterns = [
    path('game/', game_view, name='game_view'),
    path('add_author/', AddAuthor.as_view(), name='add_author'),
    path('author_page/<int:pk>/', AuthorPage.as_view(), name='author_page'),
    path('add_post/', AddPost.as_view(), name='add_post'),
]
