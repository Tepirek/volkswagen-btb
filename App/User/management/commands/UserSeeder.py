from django.core.management.base import BaseCommand
from User.factory import UserFactory
from time import time_ns


class Command(BaseCommand):

    help = 'Seeds database with User records'


    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            default=10,
            type=int,
        )


    def handle(self, *args, **options):
        start = time_ns()
        for _ in range(options['n']):
            UserFactory.create()
        end = time_ns()
        print('UserFactory seeder done: %.4fs' % ((end - start) / 1000000000))