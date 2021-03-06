from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):


    def create_user(self, worker_id, password, **extra_fields):

        if not worker_id:
            raise ValueError(_('Worker ID must be set'))
        worker_id = worker_id
        user = self.model(worker_id=worker_id, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, worker_id, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(worker_id, password, **extra_fields)
