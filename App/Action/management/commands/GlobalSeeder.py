from django.core.management.base import BaseCommand
from time import time_ns
import os

SEEDS = (
    ('ColorSeeder', None),
    ('BodyTypeSeeder', None),
    ('ErrorTypeSeeder', None),
    ('InclusionTypeSeeder', None),
    ('ComponentTypeSeeder', None),
    ('ActionSeeder', None),
    ('UserSeeder', 20),
    ('ReportSeeder', 50),
    ('PointSeeder', 500),
)


class Command(BaseCommand):

    help = 'Seeds database with multiple data records'

    def handle(self, *args, **options):
        start = time_ns()

        for seed in SEEDS:
            print(f'seeding: {seed[0]}')
            args = ' -n ' + str(seed[1]) if seed[1] else ''
            print(f'python manage.py {seed[0]}{args}')
            os.system(f'python manage.py {seed[0]}{args}')
        
        end = time_ns()

        print('GlobalSeeder seeder done %.4fs' % ((end - start) / 1000000000))