from django.db import models

from django.contrib.contenttypes.fields import GenericRelation

from reservations.models import Reservation


class Boat(models.Model):
    name = models.CharField(
        max_length=20,
    )

    reservations = GenericRelation(Reservation)
