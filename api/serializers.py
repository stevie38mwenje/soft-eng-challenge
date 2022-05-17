from rest_framework import serializers

from . import models


class MothershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mothership
        fields = '__all__'


class ShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ship
        fields = '__all__'


class CrewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CrewMember
        fields = '__all__'


