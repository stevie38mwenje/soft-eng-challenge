# Create your views here.
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import Mothership, Ship, CrewMember, ShipCrew
from .serializers import MothershipSerializer, ShipSerializer, CrewSerializer
from .utils import create_ship, create_crew


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
            shipserializer.save()
            mothership = shipserializer.data.get('mothership')
            print("mothershipdata....", mothership)
            mothership_count = Ship.objects.filter(mothership=mothership).count()
            if mothership_count > 9:
                raise ValidationError(detail='Not enough space in mothership')
            else:
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
            crewserializer.save()
            ship = crewserializer.data.get('ship')
            ship_count = CrewMember.objects.filter(ship=ship).count()
            if ship_count > 5:
                print("ship count___", ship_count)
                raise ValidationError(detail='Not enough space in ship')
            else:
                return Response(crewserializer.data, status=status.HTTP_201_CREATED)
        return Response(crewserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SwapCrewMember(APIView):
    queryset = CrewMember.objects.all()

    def put(self, request, *args, **kwargs):
        crew = self.queryset.get(pk=kwargs["pk"])
        serializer = CrewSerializer(crew, data=request.data)
        if serializer.is_valid():
            print("=====")
            ship = serializer.validated_data.pop('ship')
            if ship.has_space:
                serializer.save()
                return Response(serializer.data)
            else:
                return ValidationError(detail='no space left')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class AssignCrewMemberToShip(APIView):

    def post(self, request, **kwargs):
        try:
            print("Request Data: ", request.data)
            listmodels = []
            for line in request.data:
                model = ShipCrew(**line)
                listmodels.append(model)
            ShipCrew.objects.bulk_create(listmodels)
        except Exception as e:
            return Response({"status": "01", "message": "Unable to create crew members and assign to ship. " + repr(e)})
        return Response(data=request.data, status=HTTP_200_OK)
