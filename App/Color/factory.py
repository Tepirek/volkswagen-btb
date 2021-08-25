import factory
import factory.django
from numpy import random

from .models import Color
from User.models import User


COLORS = (
    '008',
    '100',
    'B4B4 ',
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

users = User.objects.all()

class ColorFactory(factory.django.DjangoModelFactory):
    
    name = random.choice(COLORS)

    created_by = factory.LazyAttribute(
        lambda o: random.choice(users)
    )

    class Meta:
        model = Color