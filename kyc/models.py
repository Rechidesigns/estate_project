from django.db import models
from django.utils.translation import gettext_lazy as _
from helpers.common.basemodel import BaseModel
from estate_project.users.models import User
from locations.models import Country, State

GENDER_CHOICES = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE")
)



ID_CHOICES = (
    ("DRIVERS_LISCENSE", "DRIVERS_LISCENSE"),
    ("NATIONAL_IDENTIFICATION", "NATIONAL_IDENTIFICATION"),
    ("INTERNATIONAL_PASSPORT", "INTERNATIONAL_PASSPORT")

)

PROOF_OF_ADDRESS_CHOICES = (
    ("ELECTRICITY_BILL", "ELECTRICITY BILL"),
    ("GAS_BILL", "GAS BILL"),
    ("WATER_BILL", "WATER BILL"),
    ("SEWER_BILL", "SEWER  BILL"),
    ("RECYCLING_BILL", "RECYCLING BILL"),
    ("TV_CABLE_BILL", "TV / CABLE BILL"),
)



class Kyc ( BaseModel ):

    user_detail = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name= _("User_detail"),
        null = True,
        help_text=_(' this provides the sender who is sending the message')
    )

    legal_first_name = models.CharField(
        max_length= 200,
        verbose_name= _("First Name"),
        null= True,
        blank= True,
        help_text= _("Legal first name of the user as stated on the ID."),
    )

    legal_last_name= models.CharField(
        max_length= 200,
        verbose_name=   _("Last Name"),
        null= True,
        blank= True,
        help_text= _("Legal surname or family name of the user as stated on the ID."),
    )

    address_line_1 = models.CharField(
        max_length= 300,
        verbose_name= _("Address Line 1"),
        null= True,
        blank= True,
        help_text= _("Address of the user."),
    )

    address_line_2 = models.CharField(
        max_length= 300,
        verbose_name= _("Address Line 2"),
        null= True,
        blank= True,
        help_text= _("Address of the user."),
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name= _("This holds the country where the user stays."),
        null= True,
        help_text= _("Country where the user stays."),
    )

    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        verbose_name= _("State or Province where the user stays."),
        null= True,
        help_text= _("State or province the user stays."),
    )

    zip_code = models.CharField(
        max_length= 100,
        verbose_name= _("ZIP Code or Postal code of the user."),
        null= True,
        blank= True,
        help_text= _("Zip or Postal code of the users address."),
    )

    city = models.CharField(
        max_length= 250,
        verbose_name= _("City or Town where the user stays."),
        null= True,
        blank= True,
        help_text= _("The city which the user resides."),
    )

    phone_number_1 = models.CharField(
        max_length= 100,
        verbose_name= _("Phone number 1 of the user including country code."),
        null= True,
        blank= True,
        help_text= _("The city which the user resides."),
    )

    phone_number_2 = models.CharField(
        max_length= 100,
        verbose_name= _("Phone number 2 of the user including country code."),
        null= True,
        blank= True,
        help_text= _("The city which the user resides."),
    )

    proof_of_address_type = models.CharField(
        max_length= 250,
        choices= PROOF_OF_ADDRESS_CHOICES,
        null= True,
        verbose_name= _(" Prove of address type."),
        help_text= _(" Holds the type of utility bill the user used for verifications."),
    )

    proof_of_address_file = models.FileField(
        upload_to= "photo/kyc/",
        null= True,
        verbose_name= _("Prove of Address Photo"),
        help_text= _("Prove of Address by uploading image of utility bills"),
    )

    gender = models.CharField(
        max_length=50, 
        verbose_name= _("Gender"),
        choices=GENDER_CHOICES, 
        blank=True, 
        null=True,
        help_text=_("This holds the gender of the user")
    )
    
    date_of_birth = models.DateField(
        verbose_name= _("date of birth"),
        blank=True, 
        null=True,
        help_text= _("Date of birth of user")
    )
    
    profile_image = models.ImageField(
        upload_to="photo/kyc/",
        blank=True, 
        null=True, 
        verbose_name= _("Holds the users profile image, probably a headshot photo.")
    )

    personal_references = models.CharField(
        max_length = 100,
        verbose_name= _("Personal References"),
        blank = True,
        null = True,
        help_text = _(" Personal references, their names and contact info")
    )

    rental_history = models.CharField(
        max_length = 250,
        verbose_name= _("Rental History"),
        blank = True,
        null = True,
        help_text = _("This holds the landlords and tenants previous address information")
    )

    employment_income = models.CharField(
        max_length = 100,
        verbose_name= _("Employment Income"),
        blank = True,
        null = True,
        help_text = _(" This holds the tenant employment income history, tax etc")
    )

    credit_check = models.FileField(
        verbose_name= _("credit Check"),
        upload_to = "photo/kyc/",
        blank = True,
        null = True,
        help_text = _(" This is for uploading the tenant bank statement")
    )

    criminal_security_background_check = models.FileField(
        verbose_name= _("Criminal Security Background Check"),
        upload_to = "photo/kyc/",
        blank = True,
        null = True,
        help_text = _("Holds the tenant files for background information")
    )
    
    nationality = models.CharField(
        verbose_name= _("Nationality"),
        max_length = 250,
        blank=True,
        null=True,
        help_text= _("This holds the users country of origin where the user is from")
    )
    
    second_nationality = models.CharField(
        verbose_name= _(" Second Nationality"),
        max_length = 250,
        blank=True,
        null=True,
        help_text= _("This holds the users second country of origin if the user has dual citizenship")
    )
    
    type_of_identification = models.CharField(
        max_length= 50,
        choices= ID_CHOICES,
        verbose_name= _("Type of identification ID used"),
        null= True,
        blank= True,
        help_text= _("This holds the type of identification ID used")

    )

    photo_type_of_identification = models.ImageField(
        verbose_name= _("Photo ID"),
        upload_to = "photo/kyc/",
        blank = True,
        null = True,
        help_text = _(" Tenants drivers license")
    )

    created_date = models.DateTimeField(
        auto_now_add= True,
        editable= False,
        max_length= 20,
        verbose_name= _("Date and Time"),
        help_text= _("Date and Time the user submited the KYC for verification")
    )

    status = models.BooleanField(
        verbose_name=_("Active"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" This indicates if the status option type is enabled True or False."),
    )

    def __str__(self):
        return str(self.user_detail)
    
    class Meta:
        verbose_name = _("User KYC")
        verbose_name_plural = _("User KYC")


    

