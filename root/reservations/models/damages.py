from django.db import models


class Damage(models.Model):
    resolved = models.BooleanField()

    repair_costs = models.IntegerField()

    description = models.CharField(max_length=128)
