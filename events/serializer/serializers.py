from dataclasses import field
from rest_framework import serializers
from ..models.models import Events


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Events
        fields ='__all__'