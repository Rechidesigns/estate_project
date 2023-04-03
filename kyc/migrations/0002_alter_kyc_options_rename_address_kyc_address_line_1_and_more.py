# Generated by Django 4.1.6 on 2023-04-01 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("kyc", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="kyc",
            options={"verbose_name": "User KYC", "verbose_name_plural": "User KYC"},
        ),
        migrations.RenameField(
            model_name="kyc",
            old_name="address",
            new_name="address_line_1",
        ),
        migrations.RemoveField(
            model_name="kyc",
            name="bvn",
        ),
        migrations.RemoveField(
            model_name="kyc",
            name="drivers_license",
        ),
        migrations.RemoveField(
            model_name="kyc",
            name="family_size",
        ),
        migrations.RemoveField(
            model_name="kyc",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="kyc",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="kyc",
            name="nin",
        ),
        migrations.AddField(
            model_name="kyc",
            name="address_line_2",
            field=models.CharField(
                blank=True,
                help_text="Address of the user.",
                max_length=300,
                null=True,
                verbose_name="Address",
            ),
        ),
        migrations.AddField(
            model_name="kyc",
            name="city",
            field=models.CharField(
                blank=True,
                help_text="The city which the user resides.",
                max_length=250,
                null=True,
                verbose_name="Address",
            ),
        ),
        migrations.AddField(
            model_name="kyc",
            name="legal_first_name",
            field=models.CharField(
                blank=True,
                help_text="Legal first name of the user as stated on the ID.",
                max_length=200,
                null=True,
                verbose_name="First Name",
            ),
        ),
        migrations.AddField(
            model_name="kyc",
            name="legal_last_name",
            field=models.CharField(
                blank=True,
                help_text="Legal surname or family name of the user as stated on the ID.",
                max_length=200,
                null=True,
                verbose_name="Last Name",
            ),
        ),
        migrations.AddField(
            model_name="kyc",
            name="photo_type_of_identification",
            field=models.ImageField(
                blank=True,
                help_text=" Tenants drivers license",
                null=True,
                upload_to="photo/kyc/",
                verbose_name="Photo ID",
            ),
        ),
        migrations.AddField(
            model_name="kyc",
            name="proof_of_address_file",
            field=models.FileField(
                help_text="Prove of Address by uploading image of utility bills",
                null=True,
                upload_to="photo/kyc/",
                verbose_name="Prove of Address Photo",
            ),
        ),
        migrations.AddField(
            model_name="kyc",
            name="proof_of_address_type",
            field=models.CharField(
                choices=[
                    ("ELECTRICITY_BILL", "MALE"),
                    ("GAS_BILL", "FEMALE"),
                    ("WATER_BILL", "FEMALE"),
                    ("SEWER_BILL", "FEMALE"),
                    ("RECYCLING_BILL", "FEMALE"),
                    ("RECYCLING_BILL", "FEMALE"),
                ],
                help_text=" Holds the type of utility bill the user used for verifications.",
                max_length=250,
                null=True,
                verbose_name=" Prove of address type.",
            ),
        ),
        migrations.AddField(
            model_name="kyc",
            name="second_nationality",
            field=models.CharField(
                blank=True,
                help_text="This holds the users second country of origin if the user has dual citizenship",
                max_length=250,
                null=True,
                verbose_name="Nationality",
            ),
        ),
        migrations.AddField(
            model_name="kyc",
            name="state",
            field=models.CharField(
                blank=True,
                help_text="State or province the user stays.",
                max_length=250,
                null=True,
                verbose_name="Address",
            ),
        ),
        migrations.AddField(
            model_name="kyc",
            name="type_of_identification",
            field=models.CharField(
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
        migrations.AddField(
            model_name="kyc",
            name="user_detail",
            field=models.ForeignKey(
                help_text=" this provides the sender who is sendin the message",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User_detail",
            ),
        ),
        migrations.AddField(
            model_name="kyc",
            name="zip_code",
            field=models.CharField(
                blank=True,
                help_text="Zip or Postal code of the users address.",
                max_length=100,
                null=True,
                verbose_name="Address",
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="created_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                editable=False,
                help_text="Date and Time the user submited the KYC for verification",
                max_length=20,
                verbose_name="Date and Time",
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="credit_check",
            field=models.FileField(
                blank=True,
                help_text=" This is for uploading the tenant bank statement",
                null=True,
                upload_to="photo/kyc/",
                verbose_name="credit Check",
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="criminal_security_background_check",
            field=models.FileField(
                blank=True,
                help_text="Holds the tenant files for background information",
                null=True,
                upload_to="photo/kyc/",
                verbose_name="Criminal Security Background Check",
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="date_of_birth",
            field=models.DateField(
                blank=True,
                help_text="Date of birth of user",
                null=True,
                verbose_name="date of birth",
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("MALE", "MALE"), ("FEMALE", "FEMALE")],
                help_text="This holds the gender of the user",
                max_length=50,
                null=True,
                verbose_name="gender",
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="nationality",
            field=models.CharField(
                blank=True,
                help_text="This holds the users country of origin where the user is from",
                max_length=250,
                null=True,
                verbose_name="Nationality",
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="photo/kyc/",
                verbose_name="Holds the users profile image, probably a headshot photo.",
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="rental_history",
            field=models.CharField(
                blank=True,
                help_text="This holds the landlords and tenants previous address information",
                max_length=250,
                null=True,
                verbose_name="Rental History",
            ),
        ),
    ]