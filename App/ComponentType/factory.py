from factory.django import DjangoModelFactory
import factory.django
from numpy import random
from .models import ComponentType
from User.models import User

users = User.objects.all()


class ComponentTypeFactory(DjangoModelFactory):

    created_by = factory.LazyAttribute(
        lambda o: random.choice(users)
    )

    class Meta:
        model = ComponentType
