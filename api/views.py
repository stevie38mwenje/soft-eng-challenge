from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import Mothership, Ship, CrewMember, ShipCrew
from .serializers import MothershipSerializer, ShipSerializer, CrewSerializer


class CreateMothership(APIView):

    def post(self, request):
        mothershipserializer = MothershipSerializer(data=request.data)
        if mothershipserializer.is_valid():
            mothershipserializer.save()
            return Response(mothershipserializer.data, status=status.HTTP_201_CREATED)
        return Response(mothershipserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateShip(APIView):

    def post(self, request):
        shipserializer = ShipSerializer(data=request.data)
        if shipserializer.is_valid():
            shipserializer.save()
            return Response(shipserializer.data, status=status.HTTP_201_CREATED)
        return Response(shipserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateCrewMember(APIView):
    
    def post(self, request):
        crewserializer = CrewSerializer(data=request.data)
        if crewserializer.is_valid():
            crewserializer.save()
            return Response(crewserializer.data, status=status.HTTP_201_CREATED)
        return Response(crewserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


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
