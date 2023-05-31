# Generated by Django 4.1.6 on 2023-04-29 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("maintenance", "0002_alter_maintenance_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="maintenance",
            name="landlord",
        ),
        migrations.AlterField(
            model_name="maintenance",
            name="tenant",
            field=models.ForeignKey(
                help_text=" this provides the sender who is sending the message",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Tenant_User",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Tenant",
            ),
        ),
    ]
