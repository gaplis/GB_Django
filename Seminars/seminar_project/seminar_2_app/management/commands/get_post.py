from django.core.management import BaseCommand
from seminar_2_app.models import Post


class Command(BaseCommand):
    help = 'Get post by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Post id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.filter(pk=pk)

        self.stdout.write(f'{post}')
