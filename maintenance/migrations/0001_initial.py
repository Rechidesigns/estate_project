# Generated by Django 4.1.6 on 2023-04-06 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Maintenance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="this is the unique identifier of an object",
                        primary_key=True,
                        serialize=False,
                        verbose_name="id",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Timestamp when the record was created.",
                        max_length=20,
                        verbose_name="Created Date",
                    ),
                ),
                (
                    "modified_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Modified date when the record was created.",
                        max_length=20,
                        verbose_name="Modified Date",
                    ),
                ),
                (
                    "maintenance_type",
                    models.CharField(
                        blank=True,
                        help_text="The type of maintainance issue.",
                        max_length=100,
                        null=True,
                        verbose_name="Type",
                    ),
                ),
                (
                    "issue",
                    models.CharField(
                        blank=True,
                        help_text="The isssue to be reported.",
                        max_length=100,
                        null=True,
                        verbose_name="Issues",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="The size of the family of the tenant.",
                        max_length=100,
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("reported", "Reported"),
                            ("assigned", "Assigned"),
                            ("in progress", "In Progress"),
                            ("completed", "Completed"),
                        ],
                        help_text="This is the action to take place when applying for maintenance.",
                        max_length=20,
                        null=True,
                        verbose_name="Action",
                    ),
                ),
                (
                    "status",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text=" this indicates if the status option type is enabled True or False.",
                        null=True,
                        verbose_name="Active",
                    ),
                ),
                (
                    "action_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="This is the date when the action was taken.",
                        null=True,
                        verbose_name="Action Date",
                    ),
                ),
                (
                    "landlord",
                    models.ForeignKey(
                        help_text=" this provides the recipients to which this message will be sent to",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Landlord_User",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Landlord",
                    ),
                ),
                (
                    "tenant",
                    models.ForeignKey(
                        help_text=" this provides the sender who is sendin the message",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Tenant_User",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Tenant",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tenant",
                "verbose_name_plural": "Tenants",
                "ordering": ("-created_date",),
            },
        ),
    ]
