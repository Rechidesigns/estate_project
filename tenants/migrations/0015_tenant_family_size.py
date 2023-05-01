# Generated by Django 4.1.6 on 2023-04-01 11:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tenants", "0014_delete_applicant_information"),
    ]

    operations = [
        migrations.AddField(
            model_name="tenant",
            name="family_size",
            field=models.CharField(
                blank=True,
                help_text="The size of the family of the tenant.",
                max_length=100,
                null=True,
                verbose_name="Family Size",
            ),
        ),
    ]