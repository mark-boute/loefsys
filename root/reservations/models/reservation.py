from django.conf import settings
from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


def create_reservation(reservation_object, reservation_type, user):
    Reservation.objects.create(
        content_object=reservation_object,
        object_type=reservation_type,
        user=user
    )


class Reservation(models.Model):

    BOAT = 'B'
    WETSUIT = 'W'

    # Reservable object
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    # Reservation information
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        null=True
    )

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    # fine in cents
    fine = models.IntegerField(
        null=True,
        blank=True
    )

    damage = models.ForeignKey(
        'reservations.Damage',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return str(self.user) + ", " + str(self.content_type)
