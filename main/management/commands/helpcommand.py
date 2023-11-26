from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Помогите'

    def handle(self, *args, **kwargs):
      self.stdout.write('Вот помощь')