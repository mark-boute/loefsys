from django.db import models

from django.conf import settings
from django.core import validators
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField
from localflavor.generic.models import IBANField

from utils import countries


class PaymentMethods(models.TextChoices):
    COLLECTION = 'IN', _("Collection")


class Genders(models.TextChoices):
    MALE = 'M', _("Male")
    FEMALE = 'F', _("Female")
    OTHER = 'O', _("Other")
    UNSPECIFIED = 'U', _("Prefer not to say")


class User(models.Model):
    update_date = models.DateTimeField("Last Updated")

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    # Conscribo link

    relation_number = models.IntegerField(
        unique=True,
        primary_key=True,
    )

    # ----- Registration information -----

    institution = models.CharField(
        max_length=20,
        verbose_name=_("Educational institution"),
        blank=True,
        null=True,
    )

    programme = models.CharField(
        max_length=20,
        verbose_name=_("Study programme"),
        blank=True,
        null=True,
    )

    student_number = models.CharField(
        verbose_name=_("Student number"),
        max_length=8,
        validators=[
            validators.RegexValidator(
                regex=r"(s\d{7}|[ezu]\d{6,7})",
                message=_("Enter a valid student- or e/z/u-number."),
            )
        ],
        blank=True,
        null=True,
        unique=True,
    )

    RSC_number = models.CharField(
        verbose_name=_("RSC card number"),
        max_length=9,
        blank=True,
        null=True,
        unique=True,
    )

    member_since = models.DateField()

    member_until = models.DateField()

    alumni_since = models.DateField(
        blank=True,
        null=True
    )

    payment_method = models.CharField(
        choices=PaymentMethods.choices,
        max_length=2,
    )

    remark = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )

    # ---- Address information -----

    address_street = models.CharField(
        max_length=100,
        validators=[
            validators.RegexValidator(
                regex=r"^.+ \d+.*",
                message=_("please use the format <street> <number>"),
            )
        ],
        verbose_name=_("Street and house number"),
        null=True,
    )

    address_street2 = models.CharField(
        max_length=100,
        verbose_name=_("Second address line"),
        blank=True,
        null=True,
    )

    address_postal_code = models.CharField(
        max_length=10,
        verbose_name=_("Postal code"),
        null=True,
    )

    address_city = models.CharField(
        max_length=40,
        verbose_name=_("City"),
        null=True,
    )

    address_country = models.CharField(
        max_length=2,
        choices=countries.EUROPE,
        verbose_name=_("Country"),
        null=True,
    )

    # ---- Personal information ------

    phone_number = PhoneNumberField()

    IBAN = IBANField()

    birthday = models.DateField(verbose_name=_("Birthday"), null=True)

    show_birthday = models.BooleanField(
        verbose_name=_("Display birthday"),
        help_text=_(
            "Show your birthday to other members on your profile page and "
            "in the birthday calendar"
        ),
        default=True,
    )

    profile_description = models.TextField(
        verbose_name=_("Profile text"),
        help_text=_("Text to display on your profile"),
        blank=True,
        null=True,
        max_length=4096,
    )

    initials = models.CharField(
        max_length=20,
        verbose_name=_("Initials"),
        blank=True,
        null=True,
    )

    gender = models.CharField(
        choices=Genders.choices,
        max_length=1,
    )

    # photo = models.ImageField(
    #    verbose_name=_("Photo"),
    #    upload_to=_profile_image_path,
    #    storage=get_public_storage,
    #    null=True,
    #    blank=True,
    # )

    # --- Communication preference ----

    receive_newsletter = models.BooleanField(
        verbose_name=_("Receive newsletter"),
        help_text=_("Receive the Thalia Newsletter"),
        default=True,
    )
