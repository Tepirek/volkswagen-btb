import factory
import factory.fuzzy
import factory.django
from numpy import random

from .models import InclusionType
from User.models import User

users = User.objects.all()

class InclusionTypeFactory(factory.django.DjangoModelFactory):

    created_by = factory.LazyAttribute(
        lambda o: random.choice(users)
    )

    class Meta:
        model = InclusionType
