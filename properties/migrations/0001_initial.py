# Generated by Django 4.1.6 on 2023-02-21 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Other_Amenities",
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
                    "amenity",
                    models.CharField(
                        blank=True,
                        help_text=" Amenities are things such as stores or sports facilities that are provided for people's convenience, enjoyment, or comfort. ",
                        max_length=255,
                        null=True,
                        verbose_name="Other Amenity",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text=" this indicates is the active utilities is enabled or not ",
                        null=True,
                        verbose_name="Active",
                    ),
                ),
            ],
            options={
                "verbose_name": "Out-Door Space",
                "verbose_name_plural": "Out-Door Space",
            },
        ),
        migrations.CreateModel(
            name="OutDoor_Spaces",
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
                    "outdoor_space",
                    models.CharField(
                        blank=True,
                        help_text="Outdoor space means a patio or deck, whether covered or uncovered, a yard, a walkway, or a parking lot, or a portion of any such space, that is located on or adjacent to the business premises, which space is owned, leased, or otherwise in the lawful control of the owner or operator of the business premises..",
                        max_length=255,
                        null=True,
                        verbose_name="Outdoor Space",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text=" this indicates is the active utilities is enabled or not ",
                        null=True,
                        verbose_name="Active",
                    ),
                ),
            ],
            options={
                "verbose_name": "Out-Door Space",
                "verbose_name_plural": "Out-Door Space",
            },
        ),
        migrations.CreateModel(
            name="Parking_Type",
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
                    "parking_type",
                    models.CharField(
                        blank=True,
                        help_text="parking in real estate generally refers to parking that is available to the public without any restrictions. This can mean that there is no charge for parking, or that the parking is available on a first-come, first-serve basis.",
                        max_length=255,
                        null=True,
                        verbose_name="Parking Type",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text=" this indicates is the active property type is enabled or not ",
                        null=True,
                        verbose_name="Active",
                    ),
                ),
            ],
            options={
                "verbose_name": "Parking Type",
                "verbose_name_plural": "Parking Type",
            },
        ),
        migrations.CreateModel(
            name="Property_Type",
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
                    "property_type",
                    models.CharField(
                        blank=True,
                        help_text="Property type refers to property characteristics and/or dwelling configuration, on which there can be one or more residential structures",
                        max_length=255,
                        null=True,
                        verbose_name="Property Type",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text=" this indicates is the active property type is enabled or not ",
                        null=True,
                        verbose_name="Active",
                    ),
                ),
            ],
            options={
                "verbose_name": "Properties Type",
                "verbose_name_plural": "Properties Type",
            },
        ),
        migrations.CreateModel(
            name="Utilities",
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
                    "utility",
                    models.CharField(
                        blank=True,
                        help_text="utility property means any property owned by persons or corporations and used for electric and gas production, transmission or distribution of water and other products, communications, including cable television, transportation and waste disposal.",
                        max_length=255,
                        null=True,
                        verbose_name="Utility",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text=" this indicates is the active utilities is enabled or not ",
                        null=True,
                        verbose_name="Active",
                    ),
                ),
            ],
            options={
                "verbose_name": "Utilities",
                "verbose_name_plural": "Utilities",
            },
        ),
        migrations.CreateModel(
            name="Properties",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="this is the unique identifier of an object",
                        primary_key=True,
                        serialize=False,
                        verbose_name="id",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Timestamp when the record was created.",
                        max_length=20,
                        verbose_name="Created Date",
                    ),
                ),
                (
                    "modified_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Modified date when the record was created.",
                        max_length=20,
                        verbose_name="Modified Date",
                    ),
                ),
                (
                    "address_1",
                    models.CharField(
                        help_text="the address one is basically the defualt address of the property",
                        max_length=255,
                        null=True,
                        verbose_name="Address 1",
                    ),
                ),
                (
                    "address_2",
                    models.CharField(
                        blank=True,
                        help_text="the address two is basically the address of the property, which can be optionally ",
                        max_length=255,
                        null=True,
                        verbose_name="Address 2",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        help_text="The hold the city of which the property is been uploaded for. ",
                        max_length=255,
                        null=True,
                        verbose_name="City",
                    ),
                ),
                (
                    "post_code",
                    models.CharField(
                        blank=True,
                        help_text=" A group of numbers or letters and numbers which are added to a postal address to assist the sorting of mail. ",
                        max_length=10,
                        null=True,
                        verbose_name="Post Code",
                    ),
                ),
                (
                    "number_of_unit",
                    models.CharField(
                        blank=True,
                        help_text=" A housing unit is one unit within a larger structure, such as a house, apartment, mobile home, or group of rooms, where a person or family eat, live, and sleep. ",
                        max_length=10,
                        null=True,
                        verbose_name="Number of Unit",
                    ),
                ),
                (
                    "unit_number",
                    models.CharField(
                        blank=True,
                        help_text=" The property unit number (formerly also called dwelling number) is part of your official address, and indicates which flat in the building you live in. ",
                        max_length=10,
                        null=True,
                        verbose_name=" Unit Number ",
                    ),
                ),
                (
                    "number_of_storeys",
                    models.CharField(
                        blank=True,
                        help_text=" Number of levels of living area a dwelling has above grade. Examples: A ranch is typically a 1- story dwelling or 1 story with attic. A cape is typically a 1.5 or 1.75 story home. Colonials are typically denoted with a 2 story, 2 story with attic, and 2.5 dwellings. ",
                        max_length=10,
                        null=True,
                        verbose_name="Number of Storeys",
                    ),
                ),
                (
                    "number_of_bedroom_and_bathroon",
                    models.CharField(
                        blank=True,
                        help_text=" Number of Rooms or Bathrooms means total number of rooms or bathrooms within a  property. ",
                        max_length=10,
                        null=True,
                        verbose_name="Number of Bedrooms and Bathrooms",
                    ),
                ),
                (
                    "funished",
                    models.BooleanField(
                        blank=True,
                        default=False,
                        help_text=" this indicates if the  property is funished or not  ",
                        null=True,
                        verbose_name="Funished",
                    ),
                ),
                (
                    "properties_image",
                    models.ImageField(
                        help_text="Properties  image for the current properties, which should be in PNG, JPEG, or JPG format",
                        null=True,
                        upload_to="photos/properties_image",
                        verbose_name="Property Image",
                    ),
                ),
                (
                    "properties_video",
                    models.FileField(
                        help_text="Properties  video for the current properties, which should be in mp4 format",
                        null=True,
                        upload_to="videos/properties_videos",
                        verbose_name="Property Video",
                    ),
                ),
                (
                    "neighborhood_features",
                    models.TextField(
                        blank=True,
                        help_text="this field need to be pass by the landlord to indicates  the feature of the property location",
                        null=True,
                        verbose_name="Neighborhood Features",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        help_text=" this is the country location of the property which is uploaded by the landlord ",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="locations.country",
                        verbose_name="Country",
                    ),
                ),
                (
                    "landlord",
                    models.ForeignKey(
                        help_text=" this profile belongs to the property owner who owns this property profile",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="properties_landlord",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Landlord of the property",
                    ),
                ),
                (
                    "other_amenities",
                    models.ManyToManyField(
                        blank=True,
                        help_text=" Amenities are things such as stores or sports facilities that are provided for people's convenience, enjoyment, or comfort.  ",
                        null=True,
                        to="properties.other_amenities",
                        verbose_name="Other Amenities ",
                    ),
                ),
                (
                    "outdoor_sapce",
                    models.ManyToManyField(
                        blank=True,
                        help_text=" Outdoor space means a patio or deck, whether covered or uncovered, a yard, a walkway, or a parking lot, or a portion of any such space, that is located on or adjacent to the business premises, which space is owned, leased, or otherwise in the lawful control of the owner or operator of the business premises.. ",
                        null=True,
                        to="properties.outdoor_spaces",
                        verbose_name="Outdoor Space ",
                    ),
                ),
                (
                    "parking_type",
                    models.ManyToManyField(
                        help_text=" parking in real estate generally refers to parking that is available to the public without any restrictions. This can mean that there is no charge for parking, or that the parking is available on a first-come, first-serve basis. ",
                        null=True,
                        to="properties.parking_type",
                        verbose_name="Parking Type ",
                    ),
                ),
                (
                    "property_type",
                    models.ManyToManyField(
                        help_text=" Property type refers to property characteristics and/or dwelling configuration, on which there can be one or more residential structures ",
                        null=True,
                        to="properties.property_type",
                        verbose_name="Property Type ",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        help_text=" this is the state or province location of the property which is uploaded by the landlord ",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="locations.state",
                        verbose_name="State or Province ",
                    ),
                ),
                (
                    "utilities",
                    models.ManyToManyField(
                        help_text=" Utility property as defined in 20 NYCRR 8185-1.1(199) means any property owned by persons or corporations and used for electric and gas production, transmission or distribution of water and other products, communications, including cable television, transportation and waste disposal. ",
                        null=True,
                        to="properties.utilities",
                        verbose_name="Utilities ",
                    ),
                ),
            ],
            options={
                "verbose_name": "All Landlord Properties",
                "verbose_name_plural": "All Landlord Properties",
                "ordering": ("-created_date",),
            },
        ),
    ]