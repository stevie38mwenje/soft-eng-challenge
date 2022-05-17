from .models import Ship, CrewMember


def create_ship(mothership_id):
    print("mothership______", mothership_id)
    ship = Ship.objects.create(mothership_id=mothership_id)
    for i in range(3):
        create_crew(ship=ship)
    return ship


def create_crew(ship, **kwargs):
    return CrewMember.objects.create(ship=ship, **kwargs)
