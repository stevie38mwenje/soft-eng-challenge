from django.urls import path

from .views import ListMothership, ListShip, ListCrewMember, MothershipDetail, ShipDetail, CrewDetail

urlpatterns = [
    path('mothership/', ListMothership.as_view()),
    path('ship/', ListShip.as_view()),
    path('crew/', ListCrewMember.as_view()),
    path('mothership/<int:pk>', MothershipDetail.as_view()),
    path('ship/<int:pk>', ShipDetail.as_view()),
    path('crew/<int:pk>', CrewDetail.as_view()),


]