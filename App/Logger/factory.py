import factory 
import factory.django
from numpy import random

from .models import Logger
from User.models import User
from Action.models import Action

actions = Action.objects.all()
users = User.objects.all()

class LoggerFactory(factory.django.DjangoModelFactory):

    action = factory.LazyAttribute(
        lambda o: random.choice(actions)
    )

    created_by = factory.LazyAttribute(
        lambda o: random.choice(users)
    )

    class Meta:
        model = Logger
