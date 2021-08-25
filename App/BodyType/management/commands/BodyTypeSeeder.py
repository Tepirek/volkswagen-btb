from django.core.management.base import BaseCommand
from BodyType.factory import BodyTypeFactory
from time import time_ns


BODY_TYPES = [
    { 'name': 'Doka', 'inside': 'doka_inside.jpg', 'outside': 'doka_outside.jpg' },
    { 'name': 'Kasten', 'inside': 'kasten_inside.jpg', 'outside': 'kasten_outside.jpg' },
    { 'name': 'Kombi', 'inside': 'kombi_inside.jpg', 'outside': 'kombi_outside.jpg' },
]
class Command(BaseCommand):

    help = 'Seeds database with BodyType records'


    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            default=10,
            type=int,
        )

    def handle(self, *args, **options):
        start = time_ns()
        for body_type in BODY_TYPES:
            BodyTypeFactory.create(
                name=body_type['name'],
                blueprint_inside=str('blueprints/' + body_type['inside']),
                blueprint_outside=str('blueprints/' + body_type['outside'])
            )
            print('Created: "%s"' % (body_type['name']))
        end = time_ns()
        print('BodyTypeFactory seeder done: %.4fs' % ((end - start) / 1000000000))
