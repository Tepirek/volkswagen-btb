from rest_framework import serializers
from InclusionType.models import InclusionType


class InclusionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = InclusionType
      
        fields = [
            'id',
            'name',
            'marker',
        ]
