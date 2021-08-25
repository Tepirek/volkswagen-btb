from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            'id',
            'worker_id',
            'first_name',
            'last_name',
            'email',
            'avatar',
        ]

# # POSSIBLE FIELDS

# 'id',
# 'password',
# 'last_login',
# 'is_superuser',
# 'is_staff',
# 'is_active',
# 'date_joined',
# 'worker_id',
# 'first_name',
# 'last_name',
# 'email',
# 'avatar',
# 'groups',
# 'user_permissions',
