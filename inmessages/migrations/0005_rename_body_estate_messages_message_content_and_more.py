# Generated by Django 4.1.6 on 2023-03-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inmessages", "0004_estate_messages_sender"),
    ]

    operations = [
        migrations.RenameField(
            model_name="estate_messages",
            old_name="body",
            new_name="message_content",
        ),
        migrations.AlterField(
            model_name="estate_messages",
            name="message_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("maintanance", "Maintanance"),
                    ("utilities", "Utilities"),
                    ("bills", "Bills"),
                    ("complaints", "Complaints"),
                    ("others", "Others"),
                ],
                help_text="this fields requires the message type of which the message will be sent with and categorized into",
                max_length=20,
                null=True,
                verbose_name="Message Type",
            ),
        ),
    ]