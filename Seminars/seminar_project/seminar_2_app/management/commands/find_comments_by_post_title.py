from random import randint

from django.core.management import BaseCommand

from seminar_2_app.models import Comment


class Command(BaseCommand):
    help = 'Find post by name author'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Title post')
        parser.add_argument('count', type=str, help='Count posts')

    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        count = kwargs.get('count')
        comments = Comment.objects.filter(post__title=title)
        if count == 'all':
            for c in comments:
                self.stdout.write(f'{c}')
        elif isinstance(int(count), int):
            count = count if len(comments) > int(count) else len(comments)
            for c in range(int(count)):
                self.stdout.write(f'{comments[c]}')

