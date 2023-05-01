# Generated by Django 4.1.6 on 2023-04-05 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("properties", "0013_delete_comments"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="This holds the comment made for the property",
                        null=True,
                        verbose_name="Comment",
                    ),
                ),
                (
                    "date_time",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text=" This holds time and the date the comment was made.",
                        null=True,
                        verbose_name="Date & Time",
                    ),
                ),
                (
                    "properties",
                    models.ForeignKey(
                        help_text="This holds the property the user or visitor is commenting on.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="properties.properties",
                        verbose_name="Property Comment",
                    ),
                ),
            ],
            options={
                "verbose_name": "All Property Comments",
                "verbose_name_plural": "All Properties Comments",
            },
        ),
    ]