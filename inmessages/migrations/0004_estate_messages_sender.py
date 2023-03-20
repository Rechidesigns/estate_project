# Generated by Django 4.1.6 on 2023-03-18 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("inmessages", "0003_alter_estate_messages_message_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="estate_messages",
            name="sender",
            field=models.ForeignKey(
                help_text="The sender of the message",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="message_sender",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Sender",
            ),
        ),
    ]
