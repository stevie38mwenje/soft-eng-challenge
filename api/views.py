from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import Mothership, Ship, CrewMember, ShipCrew
from .serializers import MothershipSerializer, ShipSerializer, CrewSerializer


class CreateMothership(CreateAPIView):
    serializer_class = MothershipSerializer
    queryset = Mothership.objects.all()


class CreateShip(CreateAPIView):
    serializer_class = ShipSerializer
    queryset = Ship.objects.all()


class CreateCrewMember(CreateAPIView):
    serializer_class = CrewSerializer
    queryset = CrewMember.objects.all()


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
