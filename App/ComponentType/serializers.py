from rest_framework import serializers
from ComponentType.models import ComponentType
from BodyType.serializers import BodyTypeSerializer

class ComponentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComponentType
                
        fields = [
            'id',
            'name',
            'image',
            'body_type',
            'is_inner',
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['body_type'] = BodyTypeSerializer(instance.body_type).data
        return ret
