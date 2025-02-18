from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from .models import Ship, CrewMember


def create_ship(mothership_id):
    print("mothership______", mothership_id)
    ship = Ship.objects.create(mothership_id=mothership_id)
    for i in range(3):
        create_crew(ship_id=ship)
    return ship


def create_crew(ship_id):
    return CrewMember.objects.create(ship_id=ship_id)


def swap_crew(from_ship_id, to_ship_id, crew_id):
    from_ship = get_object_or_404(Ship, id=from_ship_id)
    to_ship = get_object_or_404(Ship, id=to_ship_id)
    to_ship_count = CrewMember.objects.filter(ship=to_ship_id).count()

    print("to ship", to_ship_count)
    if to_ship_count > 5:
        raise ValidationError(detail='Not space left for the swap')
    crew = get_object_or_404(CrewMember, ship=from_ship, id=crew_id)
    print("crew", crew)
    crew.ship = to_ship
    crew.save()
    return crew
