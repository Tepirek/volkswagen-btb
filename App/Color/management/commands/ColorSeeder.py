from django.core.management.base import BaseCommand
from Color.factory import ColorFactory
from time import time_ns


COLORS = (
    '008',
    '100',
    'B4B4',
    '8E8E',
    '4B4B',
    'X3X3',
    'V7V7',
    'E3E3',
    '2T2T',
    '0P0P',
    'KTL',
    'PVC',
)


class Command(BaseCommand):

    help = 'Seeds database with Report records'

    def handle(self, *args, **options):   
        start = time_ns()  
        for color in COLORS:
            ColorFactory.create(
                name=color,
            )
        end = time_ns()
        print('ColorFactory seeder done: %.4fs' % ((end - start) / 1000000000))