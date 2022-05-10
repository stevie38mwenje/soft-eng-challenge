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
        try:
            mothershipSerializer = MothershipSerializer(data=request.data)
            if mothershipSerializer.is_valid():
                mothershipSerializer.save()
                print("REQ:", mothershipSerializer.data)
            else:
                print("INVALID REQ:", mothershipSerializer.data)
            return Response({"status": "Ok"}, status=HTTP_200_OK)
        except:
            return Response({"status": "fail"}, status=HTTP_400_BAD_REQUEST)


class CreateShip(APIView):
    # serializer_class = ShipSerializer
    # queryset = Ship.objects.all()

    def post(self, request):
        count = request.data.get('count')

        if count:
            count = int(count)
            mothership_id = request.data.get('mothership')
            ships = []
            for i in range(count):
                serializer = ShipSerializer(data={'mothership': mothership_id})
                if serializer.is_valid():
                    serializer.save()
                    ships.append(serializer.data)
            return Response(ships, status=status.HTTP_201_CREATED)
        serializer = ShipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
