from random import choice, randint
import logging
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


# Create your views here.
def heads_tails(request):
    res = choice(['Орел', 'Решка'])
    logger.info(f'Результат = {res}')
    return HttpResponse(f"{res}")


def cube(request):
    res = randint(1, 6)
    logger.info(f'Результат = {res}')
    return HttpResponse(f"{res}")


def rand_num(request):
    res = randint(0, 100)
    logger.info(f'Результат = {res}')
    return HttpResponse(f"{res}")
