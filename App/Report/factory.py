import factory
import factory.django
from numpy import random
from .models import Report
from Color.models import Color
from BodyType.models import BodyType
from User.models import User


STATES = (
    'pending',
    'done',
)

colors = Color.objects.all()
body_types = BodyType.objects.all()
users = User.objects.all()


class ReportFactory(factory.django.DjangoModelFactory):

    state = factory.LazyAttribute(
        lambda o: random.choice(STATES)
    )

    pin = factory.Faker('credit_card_number')

    color = factory.LazyAttribute(
        lambda o: random.choice(colors)
    )

    body_type = factory.LazyAttribute(
        lambda o: random.choice(body_types)
    )
    
    created_by = factory.LazyAttribute(
        lambda o: random.choice(users)
    )
    
    class Meta:
        model = Report