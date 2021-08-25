import factory
import factory.django
from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    
    worker_id = factory.Faker('name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    
    class Meta:
        model = User