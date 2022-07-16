from django.db import models

from django.contrib.contenttypes.fields import GenericRelation

from utils.sizes import SIZES
from reservations.models import Reservation


class Wetsuit(models.Model):
    reservations = GenericRelation(Reservation)

    size = models.CharField(
        max_length=32,
        choices=SIZES,
    )
