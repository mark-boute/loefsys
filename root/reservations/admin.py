from django.contrib import admin

from .models import Boat, BoatReservation, Reservation, Damage
from .models.items import *


class BoatReservationAdmin(admin.ModelAdmin):
    list_display = ["boat", "skipper"]


class ReservationAdmin(admin.ModelAdmin):
    list_display = ["user", "content_type", "start_time"]


class DamageAdmin(admin.ModelAdmin):
    list_display = ["damaged_object", "member_responsible", "description"]


admin.site.register(Boat)
admin.site.register(BoatReservation, BoatReservationAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Damage, DamageAdmin)


class WetsuitAdmin(admin.ModelAdmin):
    list_display = ["id", "size"]


admin.site.register(Wetsuit, WetsuitAdmin)
