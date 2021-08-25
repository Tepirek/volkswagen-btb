from rest_framework import serializers
from User.serializers import UserSerializer
from .models import Logger
from Action.serializers import ActionSerializer
from App.settings import DATETIME_FORMAT

class LoggerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logger
        
        fields = [
            'id',
            'action',
            'type',
            'is_visible',
            'created_at',
            'reference',
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['action'] = ActionSerializer(instance.action).data
        ret['created_at'] = instance.created_at.strftime(DATETIME_FORMAT)
        ret['created_by'] = UserSerializer(instance.created_by).data
        return ret
