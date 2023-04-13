# Generated by Django 4.1.6 on 2023-04-08 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Kyc",
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
                    "modified_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Modified date when the record was created.",
                        max_length=20,
                        verbose_name="Modified Date",
                    ),
                ),
                (
                    "legal_first_name",
                    models.CharField(
                        blank=True,
                        help_text="Legal first name of the user as stated on the ID.",
                        max_length=200,
                        null=True,
                        verbose_name="First Name",
                    ),
                ),
                (
                    "legal_last_name",
                    models.CharField(
                        blank=True,
                        help_text="Legal surname or family name of the user as stated on the ID.",
                        max_length=200,
                        null=True,
                        verbose_name="Last Name",
                    ),
                ),
                (
                    "address_line_1",
                    models.CharField(
                        blank=True,
                        help_text="Address of the user.",
                        max_length=300,
                        null=True,
                        verbose_name="Address Line 1",
                    ),
                ),
                (
                    "address_line_2",
                    models.CharField(
                        blank=True,
                        help_text="Address of the user.",
                        max_length=300,
                        null=True,
                        verbose_name="Address Line 2",
                    ),
                ),
                (
                    "zip_code",
                    models.CharField(
                        blank=True,
                        help_text="Zip or Postal code of the users address.",
                        max_length=100,
                        null=True,
                        verbose_name="ZIP Code or Postal code of the user.",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        help_text="The city which the user resides.",
                        max_length=250,
                        null=True,
                        verbose_name="City or Town where the user stays.",
                    ),
                ),
                (
                    "phone_number_1",
                    models.CharField(
                        blank=True,
                        help_text="The city which the user resides.",
                        max_length=100,
                        null=True,
                        verbose_name="Phone number 1 of the user including country code.",
                    ),
                ),
                (
                    "phone_number_2",
                    models.CharField(
                        blank=True,
                        help_text="The city which the user resides.",
                        max_length=100,
                        null=True,
                        verbose_name="Phone number 2 of the user including country code.",
                    ),
                ),
                (
                    "proof_of_address_type",
                    models.CharField(
                        choices=[
                            ("ELECTRICITY_BILL", "ELECTRICITY BILL"),
                            ("GAS_BILL", "GAS BILL"),
                            ("WATER_BILL", "WATER BILL"),
                            ("SEWER_BILL", "SEWER  BILL"),
                            ("RECYCLING_BILL", "RECYCLING BILL"),
                            ("TV_CABLE_BILL", "TV / CABLE BILL"),
                        ],
                        help_text=" Holds the type of utility bill the user used for verifications.",
                        max_length=250,
                        null=True,
                        verbose_name=" Prove of address type.",
                    ),
                ),
                (
                    "proof_of_address_file",
                    models.FileField(
                        help_text="Prove of Address by uploading image of utility bills",
                        null=True,
                        upload_to="photo/kyc/",
                        verbose_name="Prove of Address Photo",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("MALE", "MALE"), ("FEMALE", "FEMALE")],
                        help_text="This holds the gender of the user",
                        max_length=50,
                        null=True,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True,
                        help_text="Date of birth of user",
                        null=True,
                        verbose_name="date of birth",
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="photo/kyc/",
                        verbose_name="Holds the users profile image, probably a headshot photo.",
                    ),
                ),
                (
                    "personal_references",
                    models.CharField(
                        blank=True,
                        help_text=" Personal references, their names and contact info",
                        max_length=100,
                        null=True,
                        verbose_name="Personal References",
                    ),
                ),
                (
                    "rental_history",
                    models.CharField(
                        blank=True,
                        help_text="This holds the landlords and tenants previous address information",
                        max_length=250,
                        null=True,
                        verbose_name="Rental History",
                    ),
                ),
                (
                    "employment_income",
                    models.CharField(
                        blank=True,
                        help_text=" This holds the tenant employment income history, tax etc",
                        max_length=100,
                        null=True,
                        verbose_name="Employment Income",
                    ),
                ),
                (
                    "credit_check",
                    models.FileField(
                        blank=True,
                        help_text=" This is for uploading the tenant bank statement",
                        null=True,
                        upload_to="photo/kyc/",
                        verbose_name="credit Check",
                    ),
                ),
                (
                    "criminal_security_background_check",
                    models.FileField(
                        blank=True,
                        help_text="Holds the tenant files for background information",
                        null=True,
                        upload_to="photo/kyc/",
                        verbose_name="Criminal Security Background Check",
                    ),
                ),
                (
                    "nationality",
                    models.CharField(
                        blank=True,
                        help_text="This holds the users country of origin where the user is from",
                        max_length=250,
                        null=True,
                        verbose_name="Nationality",
                    ),
                ),
                (
                    "second_nationality",
                    models.CharField(
                        blank=True,
                        help_text="This holds the users second country of origin if the user has dual citizenship",
                        max_length=250,
                        null=True,
                        verbose_name=" Second Nationality",
                    ),
                ),
                (
                    "type_of_identification",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("DRIVERS_LISCENSE", "DRIVERS_LISCENSE"),
                            ("NATIONAL_IDENTIFICATION", "NATIONAL_IDENTIFICATION"),
                            ("INTERNATIONAL_PASSPORT", "INTERNATIONAL_PASSPORT"),
                        ],
                        help_text="This holds the type of identification ID used",
                        max_length=50,
                        null=True,
                        verbose_name="Type of identification ID used",
                    ),
                ),
                (
                    "photo_type_of_identification",
                    models.ImageField(
                        blank=True,
                        help_text=" Tenants drivers license",
                        null=True,
                        upload_to="photo/kyc/",
                        verbose_name="Photo ID",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Date and Time the user submited the KYC for verification",
                        max_length=20,
                        verbose_name="Date and Time",
                    ),
                ),
                (
                    "status",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text=" This indicates if the status option type is enabled True or False.",
                        null=True,
                        verbose_name="Active",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        help_text="Country where the user stays.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="locations.country",
                        verbose_name="This holds the country where the user stays.",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        help_text="State or province the user stays.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="locations.state",
                        verbose_name="State or Province where the user stays.",
                    ),
                ),
                (
                    "user_detail",
                    models.ForeignKey(
                        help_text=" this provides the sender who is sending the message",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User_detail",
                    ),
                ),
            ],
            options={
                "verbose_name": "User KYC",
                "verbose_name_plural": "User KYC",
            },
        ),
    ]
