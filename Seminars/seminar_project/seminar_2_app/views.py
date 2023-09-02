from django.http import HttpResponse
from django.shortcuts import render
from seminar_2_app.models import GameModel, Author, Post
from random import randint


# Create your views here.
def index(request):
    result = ('TAILS', 'HEAD')[randint(0, 1)]

    game = GameModel(result=result)
    game.save()

    return HttpResponse(f'{game}')


def last_games(request):
    last = GameModel().return_last(5)
    last_str = ['<br>' + str(i) for i in last]
    return HttpResponse(last_str)


def author(request):
    res = Author.objects.all()
    return HttpResponse([str(i) + '<br>' for i in res])


