from django.conf import settings
from django.db import models

from django.contrib.contenttypes.fields import GenericRelation

from reservations.models import Reservation


class BoatReservation(models.Model):
    reservations = GenericRelation(Reservation)
    boat = models.ForeignKey(
        'reservations.Boat',
        on_delete=models.CASCADE,
    )

    skipper = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True)

    # boat form information
    motor_time = models.DurationField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.boat)
