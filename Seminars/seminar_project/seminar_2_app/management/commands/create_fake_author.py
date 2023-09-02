from django.core.management import BaseCommand


from seminar_2_app.models import Author


class Command(BaseCommand):
    help = 'Generate fake authors'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count user')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(first_name=f'Name{i}',
                            last_name=f'Last Name{i}',
                            email=f'mail{i}@mail.ru',
                            bio=f'Bio{i}',
                            bd=f'2000-01-0{i}')
            author.save()

