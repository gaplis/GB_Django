import random

from django.core.management import BaseCommand
from seminar_2_app.models import Post, Author, Category


class Command(BaseCommand):
    help = 'Delete post by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='post id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.filter(pk=pk).first()
        post.delete()
        self.stdout.write(f'Done, delete post id {post.pk}: {post}')
