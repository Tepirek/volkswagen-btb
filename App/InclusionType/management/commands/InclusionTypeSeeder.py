from django.core.management.base import BaseCommand
from InclusionType.factory import InclusionTypeFactory
from time import time_ns


INCLUSION_TYPES = {
        'Koagulat'              :'koagulat.jpg',
        'Perla'                 :'perla.jpg',
        'Metal'                 :'metal.jpg',
        'Czarny klej'           :'czarny klej.jpg',
        'Czastka KTL'           :'czastka KTL.jpg',
        'Czastki brazowe'       :'czastki brazowe.jpg',
        'Cu'                    :'Cu.jpg',
        'Fosforany'             :'fosforany.jpg',
        'Czastki czarne'        :'czastki czarne.jpg',
        'Czastki szare'         :'czastki szare.jpg',
        'Czarne+metal'          :'czarne+metal.jpg',
        'Szare+metal'           :'szare+metal.jpg',
        'Czastki FL'            :'czastki FL.jpg',
        'Pod FL'                :'pod FL.jpg',
        'Wlokno'                :'wlokno.jpg',
        'PVC'                   :'PVC.jpg',
        'Wlokno niebieski'      :'wlokno niebieski.jpg',
        'Czastki BC'            :'czastki BC.jpg',
        'Zelka'                 :'zelka.jpg',
        'Multikolor'            :'multikolor.jpg',
        'Pregi'                 :'pregi.jpg',
        'Zabrudzenie PVC'       :'Zabrudzenie PVC.jpg',
}

class Command(BaseCommand):

    help = 'Seeds database with InclusionType records'
    
    def handle(self, *args, **options):
        start = time_ns()

        for key in INCLUSION_TYPES:
            InclusionTypeFactory.create(
                name=key,
                marker=str('points/' + INCLUSION_TYPES[key]),
            )

        end = time_ns()
        print('InclusionTypeFactory seeder done: %.4fs' % ((end - start) / 1000000000))
