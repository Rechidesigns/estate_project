# Imports


# Django import 
from django.db import models
from django.utils.translation import gettext_lazy as _

# Custom Apps 
from helpers.common.basemodel import BaseModel
from locations.models import Country , State
from estate_project.users.models import User




# Property Types
class Property_Type (models.Model):
    """
    this hold the property type
    """

    property_type = models.CharField(
        verbose_name= _('Property Type'),
        max_length= 255,
        null = True,
        blank= True,
        help_text=_("Property type refers to property characteristics and/or dwelling configuration, on which there can be one or more residential structures")
    )

    active = models.BooleanField(
        verbose_name=_("Active"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" this indicates is the active property type is enabled or not ")
    )


    def __str__(self):
        return str(self.property_type)
    
    class Meta:
        verbose_name = _("Properties Type")
        verbose_name_plural = _("Properties Type")



# properties parking type
class Parking_Type (models.Model):
    """
    this hold the parking type
    """

    parking_type = models.CharField(
        verbose_name= _('Parking Type'),
        max_length= 255,
        null = True,
        blank= True,
        help_text=_("parking in real estate generally refers to parking that is available to the public without any restrictions. This can mean that there is no charge for parking, or that the parking is available on a first-come, first-serve basis.")
    )

    active = models.BooleanField(
        verbose_name=_("Active"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" this indicates is the active property type is enabled or not ")
    )


    def __str__(self):
        return str(self.parking_type)
    
    class Meta:
        verbose_name = _("Parking Type")
        verbose_name_plural = _("Parking Type")





# properties parking type
class Utilities (models.Model):
    """
    this hold the properties utilities
    """

    utility = models.CharField(
        verbose_name= _('Utility'),
        max_length= 255,
        null = True,
        blank= True,
        help_text=_("utility property means any property owned by persons or corporations and used for electric and gas production, transmission or distribution of water and other products, communications, including cable television, transportation and waste disposal.")
    )

    active = models.BooleanField(
        verbose_name=_("Active"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" this indicates is the active utilities is enabled or not ")
    )


    def __str__(self):
        return str(self.utility)
    
    class Meta:
        verbose_name = _("Utilities")
        verbose_name_plural = _("Utilities")


# properties outdoor space type
class OutDoor_Spaces (models.Model):
    """
    this hold the OutDoor Space 
    """

    outdoor_space = models.CharField(
        verbose_name= _('Outdoor Space'),
        max_length= 255,
        null = True,
        blank= True,
        help_text=_("Outdoor space means a patio or deck, whether covered or uncovered, a yard, a walkway, or a parking lot, or a portion of any such space, that is located on or adjacent to the business premises, which space is owned, leased, or otherwise in the lawful control of the owner or operator of the business premises..")
    )

    active = models.BooleanField(
        verbose_name=_("Active"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" this indicates is the active utilities is enabled or not ")
    )


    def __str__(self):
        return str( self.outdoor_space )
    
    class Meta:
        verbose_name = _("Out-Door Space")
        verbose_name_plural = _("Out-Door Space")



# properties Other_Amenities type
class Other_Amenities (models.Model):
    """
    this hold the OutDoor Space 
    """

    amenity = models.CharField(
        verbose_name= _('Other Amenity'),
        max_length= 255,
        null = True,
        blank= True,
        help_text=_(" Amenities are things such as stores or sports facilities that are provided for people's convenience, enjoyment, or comfort. ")
    )

    active = models.BooleanField(
        verbose_name=_("Active"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" this indicates is the active utilities is enabled or not ")
    )


    def __str__(self):
        return str( self.amenity )
    
    class Meta:
        verbose_name = _("Out-Door Space")
        verbose_name_plural = _("Out-Door Space")





# static option
# Floor area 
FLOOR_AREA = (
    ('sq_feet', _('sq_feet')),
    ('sq_m', _('sq_m')),
)

# AC types 
AC_TYPE = (
    ('window', _('Cooling')),
    ('split', _('Split')),
    ('central', _('Central')),
    ('none', _('None'))
)



# Create your models here.

class Properties (BaseModel):
    """
    this model holds the properties list for the owner
    """

    landlord = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        verbose_name = _('Landlord of the property'),
        related_name = "properties_landlord",
        null = True,
        help_text=_(' this profile belongs to the property owner who owns this property profile')
    )

    # property addresses start here 

    address_1 = models.CharField(
        verbose_name= _('Address 1'),
        max_length= 255,
        null = True,
        help_text=_('the address one is basically the defualt address of the property')
    )

    address_2 = models.CharField(
        verbose_name= _('Address 2'),
        max_length= 255,
        null = True,
        blank= True,
        help_text=_('the address two is basically the address of the property, which can be optionally ')
    )

    # property addresses ends here 

    country = models.ForeignKey(
        Country, 
        on_delete = models.CASCADE,
        verbose_name = _('Country'),
        null = True,
        help_text=_(""" this is the country location of the property which is uploaded by the landlord """)
    )

    state = models.ForeignKey(
        State, 
        on_delete = models.CASCADE,
        verbose_name = _('State or Province '),
        null = True,
        help_text=_(""" this is the state or province location of the property which is uploaded by the landlord """)
    )

    city = models.CharField(
        verbose_name= _('City'),
        max_length= 255,
        null = True,
        blank= True,
        help_text=_('The hold the city of which the property is been uploaded for. ')
    )

    post_code = models.CharField(
        verbose_name= _('Post Code'),
        max_length= 10,
        null = True,
        blank= True,
        help_text=_(" A group of numbers or letters and numbers which are added to a postal address to assist the sorting of mail. ")
    )

    number_of_unit = models.CharField(
        verbose_name= _('Number of Unit'),
        max_length= 10,
        null = True,
        blank= True,
        help_text=_(" A housing unit is one unit within a larger structure, such as a house, apartment, mobile home, or group of rooms, where a person or family eat, live, and sleep. ")
    )

    property_type = models.ManyToManyField(
        Property_Type, 
        verbose_name = _('Property Type '),
        help_text=_(""" Property type refers to property characteristics and/or dwelling configuration, on which there can be one or more residential structures """)
    )

    unit_number = models.CharField(
        verbose_name= _(' Unit Number '),
        max_length= 10,
        null = True,
        blank= True,
        help_text=_(" The property unit number (formerly also called dwelling number) is part of your official address, and indicates which flat in the building you live in. ")
    )

    number_of_storeys = models.CharField(
        verbose_name= _('Number of Storeys'),
        max_length= 10,
        null = True,
        blank= True,
        help_text=_(" Number of levels of living area a dwelling has above grade. Examples: A ranch is typically a 1- story dwelling or 1 story with attic. A cape is typically a 1.5 or 1.75 story home. Colonials are typically denoted with a 2 story, 2 story with attic, and 2.5 dwellings. ")
    )

    number_of_bedroom_and_bathroon = models.CharField(
        verbose_name= _('Number of Bedrooms and Bathrooms'),
        max_length= 10,
        null = True,
        blank= True,
        help_text=_(" Number of Rooms or Bathrooms means total number of rooms or bathrooms within a  property. ")
    )

    parking_type = models.ManyToManyField(
        Parking_Type, 
        verbose_name = _('Parking Type '),
        help_text=_(""" parking in real estate generally refers to parking that is available to the public without any restrictions. This can mean that there is no charge for parking, or that the parking is available on a first-come, first-serve basis. """)
    )

    funished = models.BooleanField(
        verbose_name=_("Funished"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" this indicates if the  property is funished or not  ")
    )

    utilities = models.ManyToManyField(
        Utilities, 
        verbose_name = _('Utilities '),
        help_text=_(""" Utility property as defined in 20 NYCRR 8185-1.1(199) means any property owned by persons or corporations and used for electric and gas production, transmission or distribution of water and other products, communications, including cable television, transportation and waste disposal. """)
    )

    outdoor_sapce = models.ManyToManyField(
        OutDoor_Spaces, 
        verbose_name = _('Outdoor Space '),
        help_text=_(""" Outdoor space means a patio or deck, whether covered or uncovered, a yard, a walkway, or a parking lot, or a portion of any such space, that is located on or adjacent to the business premises, which space is owned, leased, or otherwise in the lawful control of the owner or operator of the business premises.. """)
    )

    other_amenities = models.ManyToManyField(
        Other_Amenities, 
        verbose_name = _('Other Amenities '),
        help_text=_(""" Amenities are things such as stores or sports facilities that are provided for people's convenience, enjoyment, or comfort.  """)
    )

    properties_image = models.ImageField(
        verbose_name = _('Property Image'),
        upload_to = "photos/properties_image",
        null =True,
        help_text= _('Properties  image for the current properties, which should be in PNG, JPEG, or JPG format')
    )

    properties_video = models.FileField(
        verbose_name = _('Property Video'),
        upload_to = "videos/properties_videos",
        null =True,
        help_text= _('Properties  video for the current properties, which should be in mp4 format')
    )

    neighborhood_features = models.TextField(
        verbose_name=_('Neighborhood Features'),
        null=True,
        blank=True,
        help_text=_("this field need to be pass by the landlord to indicates  the feature of the property location")
    )

    def __str__(self):
        return str(self.landlord)

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _('All Landlord Properties')
        verbose_name_plural = _('All Landlord Properties')





























    

    
