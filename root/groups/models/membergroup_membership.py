from django.db import models

from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from groups.models.membergroup import MemberGroup


class ActiveMembershipManager(models.Manager):
    """Custom manager that gets the currently active membergroup memberships."""

    def get_queryset(self):
        return super().get_queryset().exclude(until__lt=timezone.now().date())


class MemberGroupMembership(models.Model):
    """Describes a group membership."""

    objects = models.Manager()
    active_objects = ActiveMembershipManager()

    member = models.ForeignKey(
        "members.Member",
        on_delete=models.CASCADE,
        verbose_name=_("Member"),
    )

    group = models.ForeignKey(
        MemberGroup,
        on_delete=models.CASCADE,
        verbose_name=_("Group"),
    )

    since = models.DateField(
        verbose_name=_("Member since"),
        help_text=_("The date this member joined in this role"),
        default=timezone.now().date,
    )

    until = models.DateField(
        verbose_name=_("Member until"),
        help_text=_("A member until this time (can't be in the future)."),
        blank=True,
        null=True,
    )

    chair = models.BooleanField(
        verbose_name=_("Chair of the group"),
        default=False,
    )

    role = models.CharField(
        _("role"),
        help_text=_("The role of this member"),
        max_length=255,
        blank=True,
        null=True,
    )

    note = models.CharField(
        max_length=256,
        blank=True,
    )
