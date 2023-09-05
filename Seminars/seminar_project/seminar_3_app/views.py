from random import choice, randint

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View, DetailView
from .models import Post, Author, Comment


# Create your views here.
class HomeViews(TemplateView):
    template_name = "seminar_3_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class AboutViews(TemplateView):
    template_name = "seminar_3_app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обо мне'
        return context


class OrelViews(View):
    def get(self, request, count):
        result = [choice(['Орел', 'Решка']) for _ in range(count)]
        context = {
            'title': 'Орел и решка',
            'result': result,
        }
        return render(request, 'seminar_3_app/games.html', context)


class CubeViews(View):
    def get(self, request, count):
        result = [randint(1, 6) for _ in range(count)]
        context = {
            'title': 'Кубик',
            'result': result,
        }
        return render(request, 'seminar_3_app/games.html', context)


class RandomViews(View):
    def get(self, request, count):
        result = [randint(0, 100) for _ in range(count)]
        context = {
            'title': 'Случайное число',
            'result': result,
        }
        return render(request, 'seminar_3_app/games.html', context)


class AllAuthorPostsViews(TemplateView):
    template_name = 'seminar_3_app/posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs['id_author'])
        posts = Post.objects.filter(author=author).all()
        context['posts'] = posts
        return context


class PostViews(DetailView):
    model = Post
    template_name = 'seminar_3_app/post.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.kwargs['pk'])
        comments = Comment.objects.filter(post=post).all().order_by('-publish_date')
        context['comments'] = comments
        return context
