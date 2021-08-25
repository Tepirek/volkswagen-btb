import factory.django
from numpy import random

from .models import ErrorType
from User.models import User

users = User.objects.all()

class ErrorTypeFactory(factory.django.DjangoModelFactory):

    created_by = factory.LazyAttribute(
        lambda o: random.choice(users)
    )

    class Meta:
        model = ErrorType
