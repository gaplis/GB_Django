from random import randint

from django.core.management import BaseCommand

from seminar_2_app.models import Comment


class Command(BaseCommand):
    help = 'Find post by name author'

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, help='Name author')
        parser.add_argument('count', type=str, help='Count posts')

    def handle(self, *args, **kwargs):
        first_name = kwargs.get('first_name')
        count = kwargs.get('count')
        comments = Comment.objects.filter(author__first_name=first_name)
        if count == 'all':
            for c in comments:
                self.stdout.write(f'{c}')
        elif isinstance(int(count), int):
            count = count if len(comments) > int(count) else len(comments)
            for c in range(int(count)):
                self.stdout.write(f'{comments[c]}')

