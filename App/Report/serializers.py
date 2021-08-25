from rest_framework import serializers
from Report.models import Report
from BodyType.serializers import BodyTypeSerializer
from Color.serializers import ColorSerializer
from User.serializers import UserSerializer
from App.settings import DATETIME_FORMAT


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report

        fields = [
            'id',
            'state',
            'pin',
            'body_type',
            'color',
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['body_type'] = BodyTypeSerializer(instance.body_type).data
        ret['color'] = ColorSerializer(instance.color).data
        ret['sent_at'] = instance.sent_at.strftime(DATETIME_FORMAT) if instance.sent_at else None
        ret['created_at'] = instance.created_at.strftime(DATETIME_FORMAT)
        ret['created_by'] = UserSerializer(instance.created_by).data
        return ret


class BlueprintSerializer(serializers.Serializer):

        blueprint_inside = serializers.FileField()
        blueprint_outside = serializers.FileField()
