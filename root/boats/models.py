from django.db import models

from django.utils.translation import gettext_lazy as _


class BoatTypes(models.TextChoices):
    MOTOR = 'M', _("Motorboat")
    CABIN = 'C', _("Cabin cruiser")
    DINGHY = 'D', _("Dinghy")
    KEEL = 'K', _("Keel boat")


class Boat(models.Model):
    name = models.CharField(
        max_length=32,
    )

    boat_type = models.CharField(
        max_length=32,
        choices=BoatTypes.choices,
    )

    skippership = None  # think of a way to implement certificates

    location = models.CharField(
        max_length=64,
    )

    # fields for boats with motor
    has_motor = models.BooleanField()

    @property



class BoatDamages(models.Model):
    boat = models.ForeignKey(
        Boat,
        on_delete=models.CASCADE,
    )

    damage = models.CharField(
        max_length=128,
    )
