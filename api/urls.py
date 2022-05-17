from django.urls import path

from .views import ListMothership, ListShip, ListCrewMember, MothershipDetail, ShipDetail, CrewDetail, CreateMothership, \
    CreateShip, CreateCrewMember, DeleteShip, SwapCrewMember

urlpatterns = [
    path('mothership/', ListMothership.as_view()),
    path('ship/', ListShip.as_view()),
    path('crew/', ListCrewMember.as_view()),
    path('mothership/<int:pk>', MothershipDetail.as_view()),
    path('ship/<int:pk>', ShipDetail.as_view()),
    path('crew/<int:pk>', CrewDetail.as_view()),
    path('mothership/add', CreateMothership.as_view()),
    path('ship/add', CreateShip.as_view()),
    path('crew/add', CreateCrewMember.as_view()),
    path('ship/delete/<int:pk>', DeleteShip.as_view()),
    path('crewswap/', SwapCrewMember.as_view()),

]