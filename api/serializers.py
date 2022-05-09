from rest_framework import serializers

from human_airforce.airforce.api import models, interface


class MothershipSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return interface.create_mothership()

    class Meta:
        model = models.Mothership
        fields = '__all__'


class ShipSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        mothership_data = validated_data.pop('mothership')
        return interface.create_ship(mothership_data)

    class Meta:
        model = models.Ship
        fields = '__all__'


class CrewSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        ship_data = validated_data.pop('ship')
        return interface.create_ship(ship_data)

    class Meta:
        model = models.CrewMember
        fields = '__all__'


class ShipCrewSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = models.ShipCrew
        fields = '__all__'

