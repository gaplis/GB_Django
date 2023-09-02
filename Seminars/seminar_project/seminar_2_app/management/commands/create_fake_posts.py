import random

from django.core.management import BaseCommand

from seminar_2_app.models import Author, Post, Category


class Command(BaseCommand):
    help = 'Generate fake posts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count post')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for c in Category.objects.all():
            for a in Author.objects.all():
                for i in range(1, count + 1):
                    post = Post(title=f'Title{i}',
                                post=f'Post{i}',
                                publish_date=f'2000-01-01',
                                author=a,
                                category=c,
                                views=random.randint(1, 1000),
                                publish=random.randint(0, 1))
                    post.save()
