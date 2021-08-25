from rest_framework import serializers
from Action.models import Action


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action

        fields = [
            'id',
            'name',
            'title',
            'description',
        ]
