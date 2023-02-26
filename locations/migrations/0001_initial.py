# Generated by Django 4.1.6 on 2023-02-21 12:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                        help_text="English name of country",
                        max_length=255,
                        verbose_name="Country Name",
                    ),
                ),
                (
                    "phone_code",
                    models.CharField(
                        blank=True,
                        help_text="Countries International dialing phone code.",
                        max_length=100,
                        null=True,
                        verbose_name="Phone Code",
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        blank=True,
                        help_text="Official country currency.",
                        max_length=50,
                        null=True,
                        verbose_name="Currency",
                    ),
                ),
                (
                    "iso2",
                    models.CharField(
                        blank=True,
                        help_text="Two-letter country code",
                        max_length=2,
                        null=True,
                        verbose_name="ISO2",
                    ),
                ),
                (
                    "native",
                    models.CharField(
                        blank=True,
                        help_text="Localized or native language of country.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="Timestamp when the record was created",
                        verbose_name="Created Date",
                    ),
                ),
                (
                    "modified_date",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="Timestamp when the record was modified.",
                        verbose_name="Modified Date",
                    ),
                ),
            ],
            options={
                "verbose_name": "Country",
                "verbose_name_plural": "Countries",
                "db_table": "countries",
            },
        ),
        migrations.CreateModel(
            name="State",
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
                    "province",
                    models.CharField(
                        blank=True,
                        help_text=" this is the name of the province",
                        max_length=40,
                        null=True,
                        verbose_name="province or state ",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=False,
                        help_text="Indicate if province is active or not",
                        verbose_name="Active",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="Timestamp when the record was created",
                        verbose_name="Created Date",
                    ),
                ),
                (
                    "modified_date",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="Timestamp when the record was modified.",
                        verbose_name="Modified Date",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        help_text=" this holds the record for the country which the province belongs to ",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="locations.country",
                    ),
                ),
            ],
            options={
                "verbose_name": "Country Province or State ",
                "verbose_name_plural": "Country Province or State ",
                "db_table": "countries_province_or_state",
            },
        ),
    ]