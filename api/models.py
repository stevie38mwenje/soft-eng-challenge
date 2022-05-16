from django.db import models


# Create your models here.

class Mothership(models.Model):
    name = models.CharField(max_length=255, null=True)
    capacity = models.SmallIntegerField(default=9)

    # @property
    # def has_space(self):
    #     return self.capacity > Ship.objects.filter(mothership=self).count()


class Ship(models.Model):
    name = models.CharField(max_length=255, null=True)
    capacity = models.SmallIntegerField(default=5)
    mothership = models.ForeignKey(Mothership, on_delete=models.CASCADE)

    # @property
    # def has_space(self, ship=None):
    #     return self.capacity > CrewMember.objects.filter(ship).count()


class CrewMember(models.Model):
    name = models.CharField(max_length=255, null=True)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)

    def __str__(self):
        return 'NAME: {}'.format(self.name)


class ShipCrew(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    crew = models.ForeignKey(CrewMember, on_delete=models.CASCADE)
