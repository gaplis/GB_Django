from django.core.management import BaseCommand


from seminar_2_app.models import Author, Category


class Command(BaseCommand):
    help = 'Generate fake category'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count category')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            category = Category(name=f'Category{i}')
            category.save()

