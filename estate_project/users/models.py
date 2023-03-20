
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings

import uuid
from helpers.common.basemodel import BaseModel
from django.db.models.signals import post_save



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
    """Default user for estate management system."""
    objects = UserManager()

    ACCOUNT_TYPE = (
        ('Landlord', _('Landlord')),
        ('Tenant', _('Tenant')),
        
    )


    id = models.UUIDField(
        default = uuid.uuid4,
        editable=False,
        primary_key=True,
        help_text=_("The unique identifier of the customer.")
    )

     #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)

    email = models.EmailField(
        max_length=150,
        null=True,
        unique=True,
        verbose_name=_("Email Address"),
        help_text=_("The email address of the customer.")
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    username = None


    first_name = models.CharField(
        verbose_name=_("First names"),
        max_length=100,
        null=True,
        help_text=_("The first names of the customer.")
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name=_("Last names"),
        null=True,
        help_text=_("The last names of the customer.")
    ) 

    contact_number = models.CharField(
        max_length=100,
        verbose_name=_("Contact Number"),
        null=True,
        help_text=_("contact number of the customer.")
    ) 

    # phone = PhoneNumberField(null=True, blank=False, unique=True)

    home_address = models.CharField(
        max_length=250,
        verbose_name=_("Home Address"),
        null=True,
        blank = True,
        help_text=_("this holds the home address of the user.")
    ) 
    
    account_type = models.CharField(
        choices=ACCOUNT_TYPE,
        verbose_name=_("Account Type"),
        max_length=50,
        null=True,
        blank=True,
        help_text = _("Account type is used to identify the account user either the landlord or the tenant.")
    )

    class Meta:
        verbose_name = _("users  Account")
        verbose_name_plural = _("users  Account")

    # def __str__(self):
    #     return str(self.email)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


# GENDER_CHOICES = (
#     ("MALE", "MALE"),
#     ("FEMALE", "FEMALE")
# )


# class User_KYC( BaseModel ):
#     """
#     The user kyc is a model that is connected to the user and if the user model is deleted then
#     the user kyc will also be deleted
#     """
#     user_profile = models.OneToOneField(
#         User, on_delete=models.CASCADE,
#         related_name="user_profile",
#         null = True,
#         )

#     gender = models.CharField(
#         max_length=50, 
#         verbose_name= _("gender"),
#         choices=GENDER_CHOICES, 
#         blank=True, 
#         null=True,
#         help_text=_("gender of the user")
#         )
    
#     date_of_birth = models.DateField(
#         verbose_name= _("date of birth"),
#         blank=True, 
#         null=True,
#         help_text= _("date of birth of applicant")
#         )
    
#     profile_image = models.ImageField(
#         upload_to="user_profile_image",
#         blank=True, 
#         null=True, 
#         verbose_name= _("Holds the users profile yesterday")
#     )
    
#     nin = models.ImageField(
#         verbose_name= _("NIN"),
#         upload_to = "photos/applicant_image",
#         blank = True,
#         null = True,
#         help_text = _("National Identification Number")
#     )

#     bvn = models.CharField(
#         max_length = 100,
#         verbose_name= _("BVN"),
#         blank = True,
#         null = True,
#         help_text = _("Bank Verification Number")
#     )

#     drivers_license = models.ImageField(
#         verbose_name= _("Driver's License"),
#         upload_to = "photos/applicant_image",
#         blank = True,
#         null = True,
#         help_text = _(" Tenants drivers license")
#     )

#     family_size = models.CharField(
#         max_length = 100,
#         verbose_name= _("Family Size"),
#         blank = True,
#         null = True,
#         help_text = _("This holds the total number of the fmily or its size")
#     )

#     personal_references = models.CharField(
#         max_length = 100,
#         verbose_name= _("Personal References"),
#         blank = True,
#         null = True,
#         help_text = _(" Personal references, their names and contact info")
#     )

#     rental_history = models.CharField(
#         max_length = 250,
#         verbose_name= _("Rental History"),
#         blank = True,
#         null = True,
#         help_text = _("This holds the tenants rental history, comments, reviews and rental payment history, etc")
#     )

#     employment_income = models.CharField(
#         max_length = 100,
#         verbose_name= _("Employment Income"),
#         blank = True,
#         null = True,
#         help_text = _(" This holds the tenant employment income history, tax etc")
#     )

#     credit_check = models.ImageField(
#         verbose_name= _("credit Check"),
#         upload_to = "photos/applicant_image",
#         blank = True,
#         null = True,
#         help_text = _(" This is for uploading the tenant bank statement")
#     )

#     criminal_security_background_check = models.ImageField(
#         verbose_name= _("Criminal Security Background Check"),
#         upload_to = "photos/applicant_image",
#         blank = True,
#         null = True,
#         help_text = _("Holds the tenant files for background information")
#     )
    
#     nationality = models.CharField(
#         verbose_name= _("Nationality"),
#         max_length = 250,
#         blank=True,
#         null=True
#         )
    
#     status = models.BooleanField(
#         verbose_name=_("Active"),
#         default=False,
#         null=True,
#         blank=True,
#         help_text=_(" This indicates if the status option type is enabled True or False."),
#     )

#     def __str__(self):
#         return str(self.user_profile)

#     class Meta:
#         verbose_name = _("KYC")
#         verbose_name_plural = _("KYC")


    

#     @property
#     def profile_image_url(self):
#         #  adding this function to prevent issues when accesing the profile image if it doesnt exist
#         try:
#             image = self.profile_image.url
#         except:
#             image = None
#         return image


# def post_save_create_user_kyc(sender, instance, *args, **kwargs):
#     """
#     This creates a user profile once a user is being created
#     :param instance:  the user created or updated
#     """
#     if instance:
#         user_kyc, created = User_KYC.objects.get_or_create(user=instance)


# post_save.connect(post_save_create_user_kyc, sender=User)
