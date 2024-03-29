# Generated by Django 4.1.6 on 2023-03-17 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("properties", "0010_comments"),
        ("tenants", "0011_alter_applicant_information_date_of_birth"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="applicant_information",
            name="tenant",
        ),
        migrations.AddField(
            model_name="applicant_information",
            name="landlord",
            field=models.ForeignKey(
                help_text=" this provides the landlord details to which this application will be sent to",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Landlord_of_the_tenant",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Landlord_of_the_tenant",
            ),
        ),
        migrations.AddField(
            model_name="applicant_information",
            name="properties",
            field=models.ForeignKey(
                blank=True,
                help_text="Properties assigned to a tenant.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="properties.properties",
                verbose_name="Properties",
            ),
        ),
        migrations.AlterField(
            model_name="applicant_information",
            name="user",
            field=models.ForeignKey(
                help_text=" this provides the details of the tenant who is application informations",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Tenant_user",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Tenant_user",
            ),
        ),
    ]
