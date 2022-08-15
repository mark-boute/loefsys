from django.contrib import admin

from .models import Boat


class BoatAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']


admin.site.register(Boat, BoatAdmin)
