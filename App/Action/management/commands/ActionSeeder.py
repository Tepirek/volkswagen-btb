from django.core.management.base import BaseCommand
from Action.factory import ActionFactory
from time import time_ns


ACTIONS = [
    { 'name': 'viewReport', 'title': '', 'description': '' },
    { 'name': 'viewReports', 'title': '', 'description': '' },
    { 'name': 'addReport', 'title': 'report_created', 'description': '' },
    { 'name': 'updateReport', 'title': 'report_updated', 'description': '' },
    { 'name': 'deleteReport', 'title': 'report_deleted', 'description': '' },
    { 'name': 'viewPoint', 'title': '', 'description': '' },
    { 'name': 'viewPoints', 'title': '', 'description': '' },
    { 'name': 'addPoint', 'title': '', 'description': '' },
    { 'name': 'updatePoint', 'title': '', 'description': '' },
    { 'name': 'deletePoint', 'title': '', 'description': '' },
    { 'name': 'viewSummary', 'title': '', 'description': '' },
    { 'name': 'viewSummaies', 'title': '', 'description': '' },
    { 'name': 'addSummary', 'title': 'summary_created', 'description': '' },
    { 'name': 'updateSymmary', 'title': 'summary_updated', 'description': '' },
    { 'name': 'deleteSummary', 'title': 'summary_deleted', 'description': '' },
]


class Command(BaseCommand):

    help = 'Seeds database with Action records'

    def handle(self, *args, **options):
        start = time_ns()
        
        for action in ACTIONS:
            ActionFactory.create(
                name=action['name'],
                title=action['title'],
                description=action['description'],
            )
            print('Created: { name: %16s, title: %16s, description: %32s }' % ( action['name'], action['title'], action['description'] ))
        
        end = time_ns()
        print('ActionFactory seeder done %.4fs' % ((end - start) / 1000000000))