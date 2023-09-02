from random import randint

from django.core.management import BaseCommand


from seminar_2_app.models import GameModel


class Command(BaseCommand):
    help = 'Play gsme Head and Tails'

    def handle(self, *args, **kwargs):
        result = ('TAILS', 'HEAD')[randint(0, 1)]

        game = GameModel(result=result)
        game.save()

        self.stdout.write(f'{game}')
