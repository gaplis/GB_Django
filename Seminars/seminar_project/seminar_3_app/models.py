from datetime import date

from django.db import models
from django.db.models import Manager
from django.urls import reverse
from django.utils.timezone import now


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(max_length=1000)
    bd = models.DateField()

    objects = Manager()

    def get_absolute_url(self):
        return reverse('author_page', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=1000)
    publish_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    views = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.author} - {self.title} - {self.publish}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    publish_date = models.DateField(auto_now_add=True)
    change_date = models.DateField(default=now)

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.post.pk})

    def __str__(self):
        return f'{self.author}, {self.comment}, {self.post}'
