from django.core.management.base import BaseCommand
from Report.factory import ReportFactory
from Report.models import Report
from time import time_ns
import datetime
import random

class Command(BaseCommand):

    help = 'Seeds database with Report records'


    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            default=10,
            type=int,
        )


    def handle(self, *args, **options):     
        start = time_ns()
        for _ in range(options['n']):
            ReportFactory.create()

            report = ReportFactory.create()
            random_time = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))
            Report.objects.filter(pk=report.id).update(created_at=random_time)
        end = time_ns()
        print('ReportFactory seeder done: %.4fs' % ((end - start) / 1000000000))