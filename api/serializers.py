from rest_framework import serializers

from . import models


class MothershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mothership
        fields = ('name',)


class ShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ship
        fields = '__all__'


class CrewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CrewMember
        fields = '__all__'


class ShipCrewSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = models.ShipCrew
        fields = '__all__'

