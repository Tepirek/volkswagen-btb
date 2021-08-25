from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'worker_id',
            'password1',
            'password2',
            )


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('worker_id',)
