from django.contrib import admin

from .models import boat_reservation, damages, reservation, items


class BoatReservationAdmin(admin.ModelAdmin):
    list_display = ['boat', 'skipper']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'start_time']


class DamageAdmin(admin.ModelAdmin):
    list_display = ['damaged_object', 'member_responsible', 'description']


admin.site.register(boat_reservation.BoatReservation, BoatReservationAdmin)
admin.site.register(reservation.Reservation, ReservationAdmin)
admin.site.register(damages.Damage, DamageAdmin)


class WetsuitAdmin(admin.ModelAdmin):
    list_display = ['id', 'size']


admin.site.register(items.Wetsuit, WetsuitAdmin)
