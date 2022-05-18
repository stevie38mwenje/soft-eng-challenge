from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from airforce.api.models import Mothership, Ship, CrewMember


class TestMothership(APITestCase):
    def test_should_create_mothership(self):
        sample_mothership = {'name': "Mwenje"}
        response = self.client.post(reverse('mothership/add'), sample_mothership)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_retrieve_all_mothership(self):
        response = self.client.post(reverse('mothership'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

    def test_should_retrieve_one_mothership(self):
        response = self.create_mothership()
        res = self.client.get(reverse('mothership', kwargs={'id': response.data['id']}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        mothership = Mothership.objects.get(id=response.data['id'])
        self.assertEqual(mothership.name, res.data['name'])

    def test_should_delete_one_mothership(self):
        res = self.create_mothership()
        prev_db_count = Mothership.objects.all().count()
        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        response = self.client.delete(reverse("mothership", kwargs={'id': res.data['id']}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestShip(APITestCase):
    def test_should_create_ship(self):
        sample_ship = {'name': "Mwenje", 'mothership_id': 4}
        response = self.client.post(reverse('ship/add'), sample_ship)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_retrieve_all_ship(self):
        response = self.client.post(reverse('ship'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

    def test_should_retrieve_one_ship(self):
        response = self.create_ship()
        res = self.client.get(reverse('ship', kwargs={'id': response.data['id']}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        ship = Ship.objects.get(id=response.data['id'])
        self.assertEqual(ship.name, res.data['name'])

    def test_should_delete_one_ship(self):
        res = self.create_ship()
        prev_db_count = Ship.objects.all().count()
        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        response = self.client.delete(reverse("ship", kwargs={'id': res.data['id']}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestCrewMember(APITestCase):
    def test_should_create_crew(self):
        sample_crew = {'name': "Mwenje", 'ship_id': 4}
        response = self.client.post(reverse('crew/add'), sample_crew)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_retrieve_all_crew(self):
        response = self.client.post(reverse('crew'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)

    def test_should_retrieve_one_crew(self):
        response = self.create_crew()
        res = self.client.get(reverse('crew', kwargs={'id': response.data['id']}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        crew = CrewMember.objects.get(id=response.data['id'])
        self.assertEqual(crew.name, res.data['name'])

    def test_should_delete_one_crew(self):
        res = self.create_crew()
        prev_db_count = CrewMember.objects.all().count()
        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        response = self.client.delete(reverse("crew", kwargs={'id': res.data['id']}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_swap_crew(self):
        from_ship = self.mothership['ships'][0]
        to_ship = self.mothership['ships'][1]
        crew = self.client.post(reverse('crewswap'), {'ship': from_ship['id']}).data
        response = self.client.put(reverse('crew_list'), {'from_ship': from_ship['id'], 'to_ship': to_ship['id'], })
        self.assertEqual(response.data['ship'], to_ship['id'])
