from django.core.management.base import BaseCommand
from ErrorType.factory import ErrorTypeFactory
from time import time_ns


ERROR_TYPES = {
    'Wtracenia'                 : '',
    'Smugi'                     : 'smugi.jpg',
    'Czarny klej'               : 'czarny klej.jpg',
    'Czerwony klej'             : 'czerwony klej.jpg',
    'Wyplywki'                  : 'wyplywki.jpg' ,
    'Kraterki DLK'              : 'kraterki DLK.jpg',
    'Smugi z KTL'               : 'smugi z KTL.jpg',
    'Kratery'                   : 'kratery.jpg',
    'Zacieki'                   : 'zacieki.jpg',
    'Przegazy'                  : 'przegazy.jpg',
    'Peknieta spoina PVC'       : 'peknieta spoina PVC.jpg',
    'Niedomalowanie'            : 'niedomalowanie.jpg',
    'Zgorzelina'                : 'zgorzelina.jpg',
    'Pyl szlifierski'           : 'pyl szlifierski.jpg',
    'Piasek'                    : 'piasek.jpg',
    'Zabrwienia Spawalnicze'    : 'zabrSpawalnicze.jpg',
    'Film PVC'                  : 'Film_PVC.jpg',
    'Zabrudzenie PVC'           : 'Zabrudzenie PVC.jpg',
    'Przetrysk PVC'             : 'Przetrysk_PVC.jpg',
}

class Command(BaseCommand):

    help = 'Seeds database with ErrorType records'
    
    def handle(self, *args, **options):
        start = time_ns()

        for key in ERROR_TYPES:
            
            if ERROR_TYPES[key] != '':
                ErrorTypeFactory.create(
                    name=key,
                    marker=str('points/' + ERROR_TYPES[key]),
            )
            else:
                ErrorTypeFactory.create(
                    name=key
                )

        end = time_ns()
        print('ErrorTypeFactory seeder done: %.4fs' % ((end - start) / 1000000000))
