import random

from django.core.management import BaseCommand
from seminar_2_app.models import Post, Author, Category


class Command(BaseCommand):
    help = 'Create post'

    def add_arguments(self, parser):
        parser.add_argument('author', type=int, help='Author id')
        parser.add_argument('category', type=int, help='Category id')

    def handle(self, *args, **kwargs):
        author = Author.objects.get(pk=kwargs.get('author'))
        category = Category.objects.get(pk=kwargs.get('category'))
        post = Post(title=f'New Title',
                    post=f'New post',
                    publish_date='2000-01-01',
                    author=author,
                    category=category,
                    views=random.randint(1, 1000),
                    publish=random.randint(0, 1))
        post.save()
        self.stdout.write(f'Done, post id {post.pk}: {post}')
