# Generated by Django 4.1 on 2023-03-24 20:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="MemberGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=40, unique=True, verbose_name="Groupname"
                    ),
                ),
                ("description", models.TextField()),
                (
                    "active",
                    models.BooleanField(
                        default=False,
                        help_text="This should only be unchecked if the group has been dissolved.",
                    ),
                ),
                (
                    "contact_email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="contact email address",
                    ),
                ),
                ("display_members", models.BooleanField(default=False)),
                (
                    "since",
                    models.DateField(blank=True, null=True, verbose_name="founded in"),
                ),
                (
                    "until",
                    models.DateField(
                        blank=True, null=True, verbose_name="existed until"
                    ),
                ),
            ],
            options={
                "verbose_name": "member group",
                "verbose_name_plural": "member groups",
            },
        ),
        migrations.CreateModel(
            name="MemberGroupMembership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "chair",
                    models.BooleanField(
                        default=False, verbose_name="Chair of the group"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        help_text="The role of this member",
                        max_length=255,
                        null=True,
                        verbose_name="role",
                    ),
                ),
                (
                    "since",
                    models.DateField(
                        default=datetime.date.today,
                        help_text="The date this member joined in this role",
                        verbose_name="Member since",
                    ),
                ),
                (
                    "until",
                    models.DateField(
                        blank=True,
                        help_text="A member until this time (can't be in the future).",
                        null=True,
                        verbose_name="Member until",
                    ),
                ),
                ("note", models.CharField(blank=True, max_length=256)),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="groups.membergroup",
                        verbose_name="Group",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="membergroup",
            name="members",
            field=models.ManyToManyField(
                through="groups.MemberGroupMembership", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="membergroup",
            name="permissions",
            field=models.ManyToManyField(
                blank=True, to="auth.permission", verbose_name="permissions"
            ),
        ),
    ]
