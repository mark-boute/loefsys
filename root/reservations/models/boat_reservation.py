from django.db import models

from django.contrib.contenttypes.fields import GenericRelation

from reservations.models import Reservation
from boats.models import Boat
from users.models import User


class BoatReservation(models.Model):
    reservations = GenericRelation(Reservation)
    boat = models.ForeignKey(
        Boat,
        on_delete=models.CASCADE,
    )

    # boat form information
    motor_time = models.TimeField(
        blank=True,
        null=True,
    )

    skipper = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
