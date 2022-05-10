from django.contrib import admin

from .models import Mothership, CrewMember, Ship

admin.register(Mothership, Ship, CrewMember)(admin.ModelAdmin)
