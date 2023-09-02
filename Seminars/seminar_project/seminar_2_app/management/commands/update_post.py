import random

from django.core.management import BaseCommand
from seminar_2_app.models import Post, Author, Category


class Command(BaseCommand):
    help = 'Update post title by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='post id')
        parser.add_argument('title', type=str, help='Post title')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        title = kwargs.get('title')
        post = Post.objects.filter(pk=pk).first()
        post.title = title
        post.save()
        self.stdout.write(f'Done, update post id {post.pk}: {post}')
