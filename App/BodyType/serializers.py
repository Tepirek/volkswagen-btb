from rest_framework import serializers
from BodyType.models import BodyType


class BodyTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BodyType
        
        fields = [
            'id',
            'name',
        ]
