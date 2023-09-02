from random import randint

from django.core.management import BaseCommand

from seminar_2_app.models import Post


class Command(BaseCommand):
    help = 'Find post by name author'

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, help='Name author')
        parser.add_argument('count', type=str, help='Count posts')

    def handle(self, *args, **kwargs):
        first_name = kwargs.get('first_name')
        count = kwargs.get('count')
        posts = Post.objects.filter(author__first_name=first_name)
        if count == 'all':
            for p in posts:
                self.stdout.write(f'{p}')
        elif isinstance(int(count), int):
            count = count if len(posts) > int(count) else len(posts)
            for p in range(int(count)):
                self.stdout.write(f'{posts[p]}')

