# from human_airforce.airforce.api.models import Mothership, Ship ,CrewMember
from airforce.api.models import Mothership, CrewMember, Ship


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
