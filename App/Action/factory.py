import factory 
import factory.django
from numpy import random
from .models import Action
from User.models import User


class ActionFactory(factory.django.DjangoModelFactory):

    name = factory.Faker('name')
    
    created_by = factory.LazyAttribute(
        lambda o: random.choice(User.objects.all())
    )

    class Meta:
        model = Action
