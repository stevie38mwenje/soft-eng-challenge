from .models import Ship, CrewMember


def create_ship(mothership_id):
    print("mothership______", mothership_id)
    ship = Ship.objects.create(mothership_id=mothership_id)
    for i in range(3):
        create_crew(ship_id=ship)
    return ship


def create_crew(ship_id):
    return CrewMember.objects.create(ship_id=ship_id)
