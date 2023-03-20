# Generated by Django 4.1.6 on 2023-03-20 09:40

from django.db import migrations, models
import django.utils.timezone
import estate_project.users.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="The unique identifier of the customer.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Name of User"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="The email address of the customer.",
                        max_length=150,
                        null=True,
                        unique=True,
                        verbose_name="Email Address",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="The first names of the customer.",
                        max_length=100,
                        null=True,
                        verbose_name="First names",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="The last names of the customer.",
                        max_length=100,
                        null=True,
                        verbose_name="Last names",
                    ),
                ),
                (
                    "contact_number",
                    models.CharField(
                        help_text="contact number of the customer.",
                        max_length=100,
                        null=True,
                        verbose_name="Contact Number",
                    ),
                ),
                (
                    "home_address",
                    models.CharField(
                        blank=True,
                        help_text="this holds the home address of the user.",
                        max_length=250,
                        null=True,
                        verbose_name="Home Address",
                    ),
                ),
                (
                    "account_type",
                    models.CharField(
                        blank=True,
                        choices=[("Landlord", "Landlord"), ("Tenant", "Tenant")],
                        help_text="Account type is used to identify the account user either the landlord or the tenant.",
                        max_length=50,
                        null=True,
                        verbose_name="Account Type",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "users  Account",
                "verbose_name_plural": "users  Account",
            },
            managers=[
                ("objects", estate_project.users.models.UserManager()),
            ],
        ),
    ]
