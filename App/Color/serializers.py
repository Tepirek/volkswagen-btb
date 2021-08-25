from rest_framework import serializers
from Color.models import Color


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        
        fields = [
            'id',
            'name',
        ]

