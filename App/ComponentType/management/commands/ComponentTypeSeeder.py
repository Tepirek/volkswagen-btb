from django.core.management.base import BaseCommand
from BodyType.models import BodyType
from ComponentType.factory import ComponentTypeFactory
from time import time_ns

COMPONENTS = [

    # DOKA START - probably complete
    
    {'name': 'Bok lewy',                'path': 'doka/bok_lewy_inside.jpg',                 'is_inner': 1,      'body_type': 1},
    {'name': 'Bok lewy',                'path': 'doka/bok_lewy_outside.jpg',                'is_inner': 0,      'body_type': 1},

    {'name': 'Bok prawy',               'path': 'doka/bok_prawy_inside.jpg',                'is_inner': 1,      'body_type': 1},
    {'name': 'Bok prawy',               'path': 'doka/bok_prawy_outside.jpg',               'is_inner': 0,      'body_type': 1},

    {'name': 'Dach',                    'path': 'doka/dach_inside.jpg',                     'is_inner': 1,      'body_type': 1},
    {'name': 'Dach',                    'path': 'doka/dach_outside.jpg',                    'is_inner': 0,      'body_type': 1},

    {'name': 'Drzwi lewe przednie',     'path': 'doka/drzwi_lewe_przednie_inside.jpg',      'is_inner': 1,      'body_type': 1},
    {'name': 'Drzwi lewe przednie',     'path': 'doka/drzwi_lewe_przednie_outside.jpg',     'is_inner': 0,      'body_type': 1},

    {'name': 'Drzwi lewe',              'path': 'doka/drzwi_lewe_inside.jpg',               'is_inner': 1,      'body_type': 1},
    {'name': 'Drzwi lewe',              'path': 'doka/drzwi_lewe_outside.jpg',              'is_inner': 0,      'body_type': 1},

    {'name': 'Drzwi prawe przednie',    'path': 'doka/drzwi_prawe_przednie_inside.jpg',     'is_inner': 1,      'body_type': 1},
    {'name': 'Drzwi prawe przednie',    'path': 'doka/drzwi_prawe_przednie_outside.jpg',    'is_inner': 0,      'body_type': 1},

    {'name': 'Drzwi prawe',             'path': 'doka/drzwi_prawe_inside.jpg',              'is_inner': 1,      'body_type': 1},
    {'name': 'Drzwi prawe',             'path': 'doka/drzwi_prawe_outside.jpg',             'is_inner': 0,      'body_type': 1},

    {'name': 'Klapka wlewu',            'path': 'doka/klapka_wlewu_inside.jpg',             'is_inner': 1,      'body_type': 1},
    {'name': 'Klapka wlewu',            'path': 'doka/klapka_wlewu_outside.jpg',            'is_inner': 0,      'body_type': 1},

    {'name': 'Maska',                   'path': 'doka/maska_inside.jpg',                    'is_inner': 1,      'body_type': 1},
    {'name': 'Maska',                   'path': 'doka/maska_outside.jpg',                   'is_inner': 0,      'body_type': 1},

    {'name': 'Podloga',                 'path': 'doka/podloga_inside.jpg',                  'is_inner': 1,      'body_type': 1},
    {'name': 'Podloga',                 'path': 'doka/podloga_outside.jpg',                 'is_inner': 0,      'body_type': 1},

    {'name': 'Sciana tyl',              'path': 'doka/sciana_tyl_inside.jpg',               'is_inner': 1,      'body_type': 1},
    {'name': 'Sciana tyl',              'path': 'doka/sciana_tyl_outside.jpg',              'is_inner': 0,      'body_type': 1},

    # DOKA END


    # KASTEN START - incomplete

    {'name': 'Bok lewy',                'path': 'kasten/bok_lewy_inside.jpg',                       'is_inner': 1,      'body_type': 2},
    {'name': 'Bok lewy',                'path': 'kasten/bok_lewy_outside.jpg',                      'is_inner': 0,      'body_type': 2},

    {'name': 'Bok prawy',               'path': 'kasten/bok_prawy_inside.jpg',                      'is_inner': 1,      'body_type': 2},
    {'name': 'Bok prawy',               'path': 'kasten/bok_prawy_outside.jpg',                     'is_inner': 0,      'body_type': 2},

    {'name': 'Drzwi lewe',              'path': 'kasten/drzwi_lewe_inside.jpg',                     'is_inner': 1,      'body_type': 2},
    {'name': 'Drzwi lewe',              'path': 'kasten/drzwi_lewe_outside.jpg',                    'is_inner': 0,      'body_type': 2},

    {'name': 'Drzwi lewe przednie',     'path': 'kasten/drzwi_lewe_przednie_inside.jpg',            'is_inner': 1,      'body_type': 2},
    {'name': 'Drzwi lewe przednie',     'path': 'kasten/drzwi_lewe_przednie_outside.jpg',           'is_inner': 0,      'body_type': 2},

    {'name': 'Drzwi prawe',             'path': 'kasten/drzwi_prawe_inside.jpg',                    'is_inner': 1,      'body_type': 2},
    {'name': 'Drzwi prawe',             'path': 'kasten/drzwi_prawe_outside.jpg',                   'is_inner': 0,      'body_type': 2},

    {'name': 'Drzwi prawe przednie',    'path': 'kasten/drzwi_prawe_przednie_inside.jpg',           'is_inner': 1,      'body_type': 2},
    {'name': 'Drzwi prawe przednie',    'path': 'kasten/drzwi_prawe_przednie_outside.jpg',          'is_inner': 0,      'body_type': 2},

    {'name': 'Drzwi przesuwane',        'path': 'kasten/drzwi_przesuwane_inside.jpg',               'is_inner': 1,      'body_type': 2},
    {'name': 'Drzwi przesuwane',        'path': 'kasten/drzwi_przesuwane_outside.jpg',              'is_inner': 0,      'body_type': 2},

    {'name': 'Klapka wlewu',            'path': 'kasten/klapka_wlewu_inside.jpg',                   'is_inner': 1,      'body_type': 2},
    {'name': 'Klapka wlewu',            'path': 'kasten/klapka_wlewu_outside.jpg',                  'is_inner': 0,      'body_type': 2},

    {'name': 'Maska',                   'path': 'kasten/maska_inside.jpg',                          'is_inner': 1,      'body_type': 2},
    {'name': 'Maska',                   'path': 'kasten/maska_outside.jpg',                         'is_inner': 0,      'body_type': 2},

    {'name': 'Podloga',                 'path': 'kasten/podloga_inside.jpg',                        'is_inner': 1,      'body_type': 2},
    {'name': 'Podloga',                 'path': 'kasten/podloga_outside.jpg',                       'is_inner': 0,      'body_type': 2},

    {'name': 'Tyl',                     'path': 'kasten/tyl_outside.jpg',                           'is_inner': 0,      'body_type': 2},

    # KASTEN END


    # KOMBI START - incomplete

    {'name': 'Portal Tylny',            'path': 'portal_tylny.png',                         'is_inner': 0,      'body_type': 3},
    {'name': 'Drzwi przesowne lewe',    'path': 'drzwi_przesowne_lewe_inside.png',          'is_inner': 1,      'body_type': 3},
    {'name': 'Drzwi przesowne lewe',    'path': 'drzwi_przesowne_lewe_outside.png',         'is_inner': 0,      'body_type': 3},
    {'name': 'Drzwi przesowne prawe',   'path': 'drzwi_przesowne_prawe_inside.png',         'is_inner': 1,      'body_type': 3},
    {'name': 'Drzwi przesowne prawe',   'path': 'drzwi_przesowneprawe_outside.png',         'is_inner': 0,      'body_type': 3},

    # KOMBI END
]


class Command(BaseCommand):
    help = 'Seeds database with ComponentType records'

    def handle(self, *args, **options):
        start = time_ns()

        for component in COMPONENTS:
            ComponentTypeFactory.create(
                name=component['name'],
                image=str('components/' + component['path']),
                is_inner=component['is_inner'],
                body_type=BodyType.objects.get(pk=component['body_type'])
            )

        end = time_ns()
        print('ComponentTypeFactory seeder done: %.4fs' % ((end - start) / 1000000000))