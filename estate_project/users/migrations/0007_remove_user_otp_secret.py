# Generated by Django 4.1.6 on 2023-03-28 17:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_user_otp_secret"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="otp_secret",
        ),
    ]
