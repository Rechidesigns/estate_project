# Generated by Django 4.1.6 on 2023-03-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("properties", "0011_alter_properties_number_of_bedroom_and_bathroon_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comments",
            name="active",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text=" this indicates if the active option type is enabled or not ",
                null=True,
                verbose_name="Active",
            ),
        ),
    ]