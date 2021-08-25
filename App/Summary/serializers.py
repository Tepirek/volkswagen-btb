from rest_framework import serializers
from Summary.models import Summary
from App.settings import DATE_FORMAT

class SummaryGetSerializer(serializers.Serializer):

    type = serializers.CharField()
    date_from = serializers.DateField(
        input_formats=['%Y-%m-%d'],
        default=None
    )
    date_to = serializers.DateField(
        input_formats=['%Y-%m-%d'],
        default=None
    )
    

class SummaryTypeSerializer(serializers.Serializer):
    
    type = serializers.CharField()


class SummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Summary

        fields = [
            'id',
            'file',
            'type',
            'date_start',
            'date_end',
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['date_start'] = instance.date_start.strftime(DATE_FORMAT)
        ret['date_end'] = instance.date_end.strftime(DATE_FORMAT)
        ret['filename'] = instance.file.name.split('/')[1]
        return ret