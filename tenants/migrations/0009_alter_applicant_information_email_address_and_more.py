# Generated by Django 4.1.6 on 2023-03-15 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tenants", "0008_alter_applicant_information_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicant_information",
            name="email_address",
            field=models.CharField(
                blank=True,
                help_text=" Holds the email address of the tenant",
                max_length=250,
                null=True,
                verbose_name="Email",
            ),
        ),
        migrations.AlterField(
            model_name="applicant_information",
            name="user",
            field=models.ForeignKey(
                blank=True,
                help_text=" this provides who this message is sent to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Landlord_form",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Landlord_form",
            ),
        ),
    ]