# from human_airforce.airforce.api.models import Mothership, Ship ,CrewMember
from rest_framework.exceptions import MethodNotAllowed, bad_request, ValidationError

from .models import Mothership, CrewMember, Ship


def create_mothership():
    mothership = Mothership.objects.create()
    mothership.save()
    return mothership


def create_crew(ship, kwargs=None):
    if ship.has_space:
        crew = CrewMember.objects.create(ship)
        for new_member in range(9):
            create_crew(ship, **kwargs)
            return crew


def create_ship(mothership):
    if mothership.has_space:
        ship = Ship.object.create(mothership)
        for new_ship in range(3):
            create_crew(ship=ship)
            return ship


def swap_crew_member(from_ship, to_ship, crew_member_name):
    from_ship = Ship.object.get(Ship, id=from_ship)
    to_ship = Ship.object.get(Ship, id=to_ship)
    if to_ship.has_space:
        crew_member = CrewMember.object.get(CrewMember, ship=from_ship, crew_member_name=crew_member_name)
        crew_member.ship = to_ship
        crew_member.save()
        return crew_member
    else:
        raise ValidationError(detail='no vacancy')
