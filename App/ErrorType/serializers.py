from rest_framework import serializers
from ErrorType.models import ErrorType


class ErrorTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ErrorType
            
        fields = [
            'id',
            'name',
            'marker',
        ]
