from rest_framework import serializers
from Point.models import Point
from ErrorType.serializers import ErrorTypeSerializer
from InclusionType.serializers import InclusionTypeSerializer
from ComponentType.serializers import ComponentTypeSerializer
from ErrorType.models import ErrorType
from InclusionType.models import InclusionType
from App.settings import DATETIME_FORMAT


class PointSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Point

        fields = [
            'id',
            'x',
            'y',
            'error_type',
            'inclusion_type',
            'component_type',
            'report',
            'stage',
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['error_type'] = ErrorTypeSerializer(instance.error_type).data
        ret['inclusion_type'] = InclusionTypeSerializer(instance.inclusion_type).data
        ret['component_type'] = ComponentTypeSerializer(instance.component_type).data
        ret['created_at'] = instance.created_at.strftime(DATETIME_FORMAT)
        return ret


class PointSummarySerializer(serializers.Serializer):

    stage=serializers.IntegerField()
    error_type=serializers.IntegerField()
    inclusion_type=serializers.IntegerField()
    amount=serializers.IntegerField()


    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['error_type'] = None
        ret['inclusion_type'] = None
        if instance['error_type']:
            ret['error_type'] = ErrorTypeSerializer(
                ErrorType.objects.get(pk=instance['error_type'])
            ).data
        if instance['inclusion_type']:
            ret['inclusion_type'] = InclusionTypeSerializer(
                InclusionType.objects.get(pk=instance['inclusion_type'])
            ).data
        return ret
