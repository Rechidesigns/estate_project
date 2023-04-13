# Imports

# Django import 
from django.db import models
from django.utils.translation import gettext_lazy as _

# Custom Apps 
from helpers.common.basemodel import BaseModel
from locations.models import Country , State
from estate_project.users.models import User



class Property_Options ( models.Model ):
    """
    this hold the property type
    """

    option = models.CharField(
        verbose_name= _('Option Type'),
        max_length= 255,
        null = True,
        blank= True,
        help_text=_("Option type refers to property options that will be used during uploading of properties by the property owner or landlord ")
    )

    active = models.BooleanField(
        verbose_name=_("Active"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" this indicates if the active option type is enabled or not ")
    )

    # def __str__(self):
    #     return self.id
    
    def __str__(self):
        return str(self.option)

    class Meta:
        abstract = True
        


# Property Types
class Property_Type (Property_Options):
    # this function holds the property type
    class Meta:
        verbose_name = _("Properties Type")
        verbose_name_plural = _("Properties Type")



# properties parking type
class Parking_Type (Property_Options): 
    # this function holds the parking type 
    class Meta:
        verbose_name = _("Parking Type")
        verbose_name_plural = _("Parking Type")


# properties parking type
class Utilities (Property_Options):
    # this function holds the utilities
    class Meta:
        verbose_name = _("Utilities")
        verbose_name_plural = _("Utilities")


# properties outdoor space type
class OutDoor_Spaces (Property_Options):
    # this function holds the outdoor space
      
    class Meta:
        verbose_name = _("Out-Door Space")
        verbose_name_plural = _("Out-Door Space")



# properties appliances type
class Appliances (Property_Options):
    # this function holds the appliances
      
    class Meta:
        verbose_name = _("appliances")
        verbose_name_plural = _("appliances")



# properties Other_Amenities type
class Other_Amenities (Property_Options):
    # this function holds the other amenities
      
    class Meta:
        verbose_name = _("Other Amenities Space")
        verbose_name_plural = _("Other Amenities Space")



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

    amount = models.DecimalField(
        verbose_name = _("Amount "),
        null=True, blank=True,
        max_digits = 300, decimal_places = 2,
        default=0.00,
        help_text=_("this is the rent fee that will be paid by the tenant")
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
        max_length= 100,
        null = True,
        blank= True,
        help_text=_(" Number of levels of living area a dwelling has above grade. Examples: A ranch is typically a 1- story dwelling or 1 story with attic. A cape is typically a 1.5 or 1.75 story home. Colonials are typically denoted with a 2 story, 2 story with attic, and 2.5 dwellings. ")
    )

    number_of_bedroom_and_bathroon = models.CharField(
        verbose_name= _('Number of Bedrooms and Bathrooms'),
        max_length= 100,
        null = True,
        blank= True,
        help_text=_(" Number of Rooms or Bathrooms means total number of rooms or bathrooms within a  property. ")
    )

    floor_area = models.CharField(
        choices= FLOOR_AREA,
        verbose_name= _('Floor Area'),
        max_length= 20,
        null = True,
        blank= True,
        help_text=_(" This is the floor area of the property")
    )

    ac_type = models.CharField(
        choices= AC_TYPE,
        verbose_name= _('AC Type'),
        max_length= 20,
        null = True,
        blank= True,
        help_text=_(" This is the ac type of the property")
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

    appliances = models.ManyToManyField(
        Appliances, 
        verbose_name = _('Appliances'),
        help_text=_(""" Appliances are device or piece of equipment designed to perform a specific task. electrical and gas appliances" """)
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
        blank=True,
        help_text= _('Properties  image for the current properties, which should be in PNG, JPEG, or JPG format')
    )

    properties_video = models.FileField(
        verbose_name = _('Property Video'),
        upload_to = "videos/properties_videos",
        null =True,
        blank=True,
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




class PropertyImage(BaseModel):
    # adding property multiple images
    property = models.ForeignKey(
        Properties, on_delete=models.CASCADE,
        null=True,
        verbose_name=_("Property"),
        help_text=_("Product of which the images belongs to.")
    )

    image = models.ImageField(
        verbose_name = _('Product Image'),
        upload_to = "photos/properties_image",
        null =True,
        help_text= _('Properties  image for the current properties, which should be in PNG, JPEG, or JPG format')
    )

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Property Image")
        verbose_name_plural = _("Property Images")

    def __str__(self):
        return str(self.property)
        
    # image compressor
    # def save(self, *args, **kwargs):
    #     if self.image:
    #         super().save(*args, **kwargs)
    #         # Image.open() can also open other image types
    #         img = Image.open(self.image.path)
    #         # WIDTH and HEIGHT are integers
    #         resized_img = img.resize((640, 640))
    #         resized_img.save(self.image.path)

























    

    
