# Generated by Django 4.1.6 on 2023-02-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("properties", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="properties",
            name="other_amenities",
            field=models.ManyToManyField(
                help_text=" Amenities are things such as stores or sports facilities that are provided for people's convenience, enjoyment, or comfort.  ",
                to="properties.other_amenities",
                verbose_name="Other Amenities ",
            ),
        ),
        migrations.AlterField(
            model_name="properties",
            name="outdoor_sapce",
            field=models.ManyToManyField(
                help_text=" Outdoor space means a patio or deck, whether covered or uncovered, a yard, a walkway, or a parking lot, or a portion of any such space, that is located on or adjacent to the business premises, which space is owned, leased, or otherwise in the lawful control of the owner or operator of the business premises.. ",
                to="properties.outdoor_spaces",
                verbose_name="Outdoor Space ",
            ),
        ),
        migrations.AlterField(
            model_name="properties",
            name="parking_type",
            field=models.ManyToManyField(
                help_text=" parking in real estate generally refers to parking that is available to the public without any restrictions. This can mean that there is no charge for parking, or that the parking is available on a first-come, first-serve basis. ",
                to="properties.parking_type",
                verbose_name="Parking Type ",
            ),
        ),
        migrations.AlterField(
            model_name="properties",
            name="property_type",
            field=models.ManyToManyField(
                help_text=" Property type refers to property characteristics and/or dwelling configuration, on which there can be one or more residential structures ",
                to="properties.property_type",
                verbose_name="Property Type ",
            ),
        ),
        migrations.AlterField(
            model_name="properties",
            name="utilities",
            field=models.ManyToManyField(
                help_text=" Utility property as defined in 20 NYCRR 8185-1.1(199) means any property owned by persons or corporations and used for electric and gas production, transmission or distribution of water and other products, communications, including cable television, transportation and waste disposal. ",
                to="properties.utilities",
                verbose_name="Utilities ",
            ),
        ),
    ]
