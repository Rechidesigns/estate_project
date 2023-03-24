from django.db import models
from django.utils.translation import gettext_lazy as _
from helpers.common.basemodel import BaseModel
from estate_project.users.models import User



GENDER_CHOICES = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE")
)



class Kyc ( BaseModel ):

    # user_id = models.CharField(
    #     max_length= 200,
    #     null = True,
    #     )
    
    first_name = models.CharField(
        max_length= 200,
        verbose_name= _("First Name"),
        null= True,
        blank= True,
        help_text= _("First name of the user."),
    )

    last_name= models.CharField(
        max_length= 200,
        verbose_name=   _("Last Name"),
        null= True,
        blank= True,
        help_text= _("Surname or family name of the user."),
    )

    address = models.CharField(
        max_length= 300,
        verbose_name= _("Address"),
        null= True,
        blank= True,
        help_text= _("Address of the user."),
    )

    gender = models.CharField(
        max_length=50, 
        verbose_name= _("gender"),
        choices=GENDER_CHOICES, 
        blank=True, 
        null=True,
        help_text=_("gender of the user")
        )
    
    date_of_birth = models.DateField(
        verbose_name= _("date of birth"),
        blank=True, 
        null=True,
        help_text= _("date of birth of applicant")
        )
    
    profile_image = models.ImageField(
        upload_to="user_profile_image",
        blank=True, 
        null=True, 
        verbose_name= _("Holds the users profile yesterday")
    )
    
    nin = models.ImageField(
        verbose_name= _("NIN"),
        upload_to = "photos/applicant_image",
        blank = True,
        null = True,
        help_text = _("National Identification Number")
    )

    bvn = models.CharField(
        max_length = 100,
        verbose_name= _("BVN"),
        blank = True,
        null = True,
        help_text = _("Bank Verification Number")
    )

    drivers_license = models.ImageField(
        verbose_name= _("Driver's License"),
        upload_to = "photos/applicant_image",
        blank = True,
        null = True,
        help_text = _(" Tenants drivers license")
    )

    family_size = models.CharField(
        max_length = 100,
        verbose_name= _("Family Size"),
        blank = True,
        null = True,
        help_text = _("This holds the total number of the fmily or its size")
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
        help_text = _("This holds the tenants rental history, comments, reviews and rental payment history, etc")
    )

    employment_income = models.CharField(
        max_length = 100,
        verbose_name= _("Employment Income"),
        blank = True,
        null = True,
        help_text = _(" This holds the tenant employment income history, tax etc")
    )

    credit_check = models.ImageField(
        verbose_name= _("credit Check"),
        upload_to = "photos/applicant_image",
        blank = True,
        null = True,
        help_text = _(" This is for uploading the tenant bank statement")
    )

    criminal_security_background_check = models.ImageField(
        verbose_name= _("Criminal Security Background Check"),
        upload_to = "photos/applicant_image",
        blank = True,
        null = True,
        help_text = _("Holds the tenant files for background information")
    )
    
    nationality = models.CharField(
        verbose_name= _("Nationality"),
        max_length = 250,
        blank=True,
        null=True
        )
    
    status = models.BooleanField(
        verbose_name=_("Active"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" This indicates if the status option type is enabled True or False."),
    )

