import factory
import factory.django
from numpy import random
from .models import Point
from Report.models import Report
from ErrorType.models import ErrorType
from InclusionType.models import InclusionType
from ComponentType.models import ComponentType
from User.models import User

users = User.objects.all()
error_types = ErrorType.objects.all()
inclusion_types = InclusionType.objects.all()
component_types = ComponentType.objects.all()
reports = Report.objects.all()


class PointFactory(factory.django.DjangoModelFactory):

    x = factory.Faker('pyint', min_value=0, max_value=100)
    
    y = factory.Faker('pyint', min_value=0, max_value=100)

    error_type = factory.LazyAttribute(
        lambda o: random.choice(error_types)
    )

    inclusion_type = factory.LazyAttribute(
        lambda o: random.choice(inclusion_types)
    )

    component_type = factory.LazyAttribute(
        lambda o: random.choice(component_types)
    )
    
    stage = factory.LazyAttribute(
        lambda o: random.randint(low=1, high=5)
    )

    report = factory.LazyAttribute(
        lambda o: random.choice(reports)
    )

    created_by = factory.LazyAttribute(
        lambda o: random.choice(users)
    )
    
    class Meta:
        model = Point