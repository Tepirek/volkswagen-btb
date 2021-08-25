import factory
import factory.django
from numpy import random
from .models import BodyType
from User.models import User

TYPES = (
    'Doka',
    'Kasten',
    'Kombi',
)

users = User.objects.all()

class BodyTypeFactory(factory.django.DjangoModelFactory):

    name = random.choice(TYPES)

    created_by = factory.LazyAttribute(
        lambda o: random.choice(users)
    )
       
    class Meta:
        model = BodyType
