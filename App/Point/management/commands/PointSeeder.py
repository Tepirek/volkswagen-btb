from django.core.management.base import BaseCommand
from Point.factory import PointFactory
from Point.models import Point
from time import time_ns
import datetime
import random

class Command(BaseCommand):

    help = 'Seeds database with Point records'


    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            default=10,
            type=int,
        )


    def handle(self, *args, **options):     
        start = time_ns()
        for _ in range(options['n']):
            point = PointFactory.create()
            random_time = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))
            Point.objects.filter(pk=point.id).update(created_at=random_time)
        end = time_ns()
        print('PointFactory seeder done: %.4fs' % ((end - start) / 1000000000))
