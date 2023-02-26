# Generated by Django 4.1.6 on 2023-02-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                help_text="The first names of the customer.",
                max_length=50,
                null=True,
                verbose_name="First names",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                help_text="The last names of the customer.",
                max_length=50,
                null=True,
                verbose_name="Last names",
            ),
        ),
    ]