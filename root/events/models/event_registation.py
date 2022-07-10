from django.db import models
from django.db.models import Q

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .event import Event
from users.models import User


def registration_user_choices_limit():
    """Define queryset filters to only include current members."""
    return Q(membership__until__isnull=True) | Q(
        membership__until__gt=timezone.now().date()
    )


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, models.CASCADE)

    user = models.ForeignKey(
        User,
        models.CASCADE,
        blank=True,
        null=True,
        limit_choices_to=registration_user_choices_limit,
    )

    date = models.DateTimeField(_("registration date"), default=timezone.now)
    date_cancelled = models.DateTimeField(_("cancellation date"), null=True, blank=True)

    present = models.BooleanField(_("present"), default=False,)
