from django.db import models

from users.models import User
from committees.models.committee import Committee


class CommitteeMembership(models.Model):
    user = models.ForeignKey(
        User,
        models.CASCADE,
        blank=True,
        null=True,
    )

    committee = models.ForeignKey(
        Committee,
        models.CASCADE,
    )

    since = models.DateField()

    until = models.DateField(
        null=True,
        blank=True,
    )
