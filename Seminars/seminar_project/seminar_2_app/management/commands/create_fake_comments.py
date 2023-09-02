from random import randint

from django.core.management import BaseCommand

from seminar_2_app.models import Author, Post, Comment


class Command(BaseCommand):
    help = 'Generate fake comments'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count comments')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        authors = [a for a in Author.objects.all()]
        posts = [p for p in Post.objects.all()]
        for i in range(1, count + 1):
            comment = Comment(author=authors[randint(1, len(authors) - 1)],
                              post=posts[randint(1, len(posts) - 1)],
                              comment=f'Comment{i}',
                              )
            comment.save()
