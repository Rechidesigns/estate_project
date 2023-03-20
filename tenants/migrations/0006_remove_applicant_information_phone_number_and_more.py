# Generated by Django 4.1.6 on 2023-03-15 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tenants", "0005_alter_applicant_information_credit_check_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="applicant_information",
            name="Phone_number",
        ),
        migrations.AddField(
            model_name="applicant_information",
            name="contact_number",
            field=models.CharField(
                blank=True,
                help_text=" Holds tenants contact Number",
                max_length=100,
                null=True,
                verbose_name="Contact Number",
            ),
        ),
        migrations.AlterField(
            model_name="applicant_information",
            name="user",
            field=models.ForeignKey(
                help_text=" this provides who this message is sent to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Tenants_form",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Tenant_form",
            ),
        ),
    ]
