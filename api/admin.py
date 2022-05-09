from django.contrib import admin

from airforce.api.models import Mothership, Ship, CrewMember

admin.register(Mothership, Ship, CrewMember)(admin.ModelAdmin)
