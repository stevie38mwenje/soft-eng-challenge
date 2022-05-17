# Create your views here.
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import Mothership, Ship, CrewMember
from .serializers import MothershipSerializer, ShipSerializer, CrewSerializer
from .utils import create_ship, create_crew, swap_crew


class CreateMothership(APIView):

    def post(self, request):
        mothershipserializer = MothershipSerializer(data=request.data)
        if mothershipserializer.is_valid():
            mothershipserializer.save()
            mothership = mothershipserializer
            for i in range(3):
                print("mothership data++++", mothership.data.get('id'))
                mothership_id = mothership.data.get('id')
                create_ship(mothership_id=mothership_id)
            return Response(mothershipserializer.data, status=status.HTTP_201_CREATED)
        return Response(mothershipserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateShip(APIView):

    def post(self, request):
        shipserializer = ShipSerializer(data=request.data)
        if shipserializer.is_valid():
            mothership = shipserializer.validated_data.get('mothership')
            print("mothershipdata....", mothership)
            mothership_count = Ship.objects.filter(mothership=mothership).count()
            mothership_capacity = mothership.capacity
            print("mothership capacity.....", mothership_capacity)
            if mothership_count > mothership_capacity:
                raise ValidationError(detail='Not enough space in mothership')
            else:
                shipserializer.save()
                for i in range(3):
                    print("ship data++++", shipserializer.data.get('id'))
                    ship_id = shipserializer.data.get('id')
                    create_crew(ship_id=ship_id)
                return Response(shipserializer.data, status=status.HTTP_201_CREATED)
        return Response(shipserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCrewMember(APIView):

    def post(self, request):
        crewserializer = CrewSerializer(data=request.data)

        if crewserializer.is_valid():
            ship = crewserializer.validated_data.get('ship')
            ship_count = CrewMember.objects.filter(ship=ship).count()
            ship_capacity = ship.capacity
            print("ship capacity.....", ship_capacity)
            if ship_count > ship_capacity:
                print("ship count___", ship_count)
                raise ValidationError(detail='Not enough space in ship')
            else:
                crewserializer.save()
                return Response(crewserializer.data, status=status.HTTP_201_CREATED)
        return Response(crewserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SwapCrewMember(APIView):
    # queryset = CrewMember.objects.all()

    # def put(self, request, *args, **kwargs):
    #     crew = self.queryset.get(pk=kwargs["pk"])
    #     serializer = CrewSerializer(crew, data=request.data)
    #     if serializer.is_valid():
    #         print("=====")
    #         ship = serializer.validated_data.pop('ship')
    #         ship_count = CrewMember.objects.filter(ship=ship).count()
    #         ship_capacity = ship.capacity
    #         if ship_count > ship_capacity:
    #             return ValidationError(detail='no space left')
    #         else:
    #             serializer.save()
    #             return Response(serializer.data,status=status.HTTP_200_OK)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        try:
            from_ship_id = request.data['from_ship']
            to_ship_id = request.data['to_ship']
            name = request.data['name']
        except KeyError as e:
            return Response(
                {"status": "failed", "status_code": 1, "message": "Cannot swap crew", "error": str(e)},
                status=HTTP_400_BAD_REQUEST)
        crew = swap_crew(from_ship_id, to_ship_id, name)
        serializer = CrewSerializer(crew)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class ListMothership(ListAPIView):
    serializer_class = MothershipSerializer
    queryset = Mothership.objects.all()


class ListShip(ListAPIView):
    serializer_class = ShipSerializer
    queryset = Ship.objects.all()


class ListCrewMember(ListAPIView):
    serializer_class = CrewSerializer
    queryset = CrewMember.objects.all()


class MothershipDetail(RetrieveAPIView):
    serializer_class = MothershipSerializer
    queryset = Mothership.objects.all()


class ShipDetail(RetrieveAPIView):
    serializer_class = ShipSerializer
    queryset = Ship.objects.all()


class CrewDetail(RetrieveAPIView):
    serializer_class = CrewSerializer
    queryset = Ship.objects.all()


class DeleteShip(RetrieveDestroyAPIView):
    serializer_class = ShipSerializer
    queryset = Ship.objects.all()
