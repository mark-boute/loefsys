from django.db import models


class Damage(models.Model):
    resolved = models.BooleanField()

    repair_costs = models.IntegerField()

    description = models.CharField(max_length=128)

    @property
    def damaged_object(self):
        return None  # TODO

    @property
    def member_responsible(self):
        return None  # TODO

    def __str__(self):
        return str(self.damaged_object) + ", " + str(self.member_responsible)
