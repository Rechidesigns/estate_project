from django.db import models
from django.utils.translation import gettext_lazy as _

# Custom Apps 
from helpers.common.basemodel import BaseModel
from estate_project.users.models import User
from properties.models import Properties


PROPERTY_ACTION = (

        ("rented", _("Rented")),
        ("processing", _("Processing")),
        ("declined", _("Declined")),
        ("review", _("Review")),
        
    )


class Tenant( BaseModel ):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name= _("Tenant"),
        related_name= "Tenant",
        null = True,
        help_text=_(' this provides the sender who is sendin the message')
    )

    landlord = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name= _("Landlord"),
        related_name= "Landlord_properties",
        null = True,
        help_text=_(' this provides the recipients to which this message will be sent to')
    )

    properties = models.ForeignKey(
        Properties,
        on_delete=models.CASCADE,
        verbose_name= _("Properties"),
        null = True,
        blank = True,
        help_text= _("Properties assigned to a tenant."),
    )

    action = models.CharField(
        choices= PROPERTY_ACTION,
        verbose_name= _("Action"),
        max_length= 20,
        null= True,
        blank= True,
        help_text= _("This is the action to take place when applying for this property."),
    )

    status = models.BooleanField(
        verbose_name=_("Active"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" this indicates if the status option type is enabled True or False."),
    )

    action_date = models.DateTimeField(
        verbose_name= _("Action Date"),
        auto_now_add= True,
        null= True,
        blank= True,
        help_text= _("This is the date when the action was taken."),
    )
    
    notification = models.BooleanField(
        verbose_name= _("Notification"),
        default= False,
        null= True,
        blank= True,
        help_text= _("This indicates if the notification option type is enabled True or False."),

    )

    
    def __str__(self):
        return str(self.user)

    
    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Tenant")
        verbose_name_plural = _("Tenants")




# class Applicant_Information ( models.Model ):

#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         verbose_name= _("Tenant_user"),
#         related_name= "Tenant_user",
#         null = True,
#         help_text=_(' this provides the details of the tenant who is application informations')
#     )

#     # landlord = models.ForeignKey(
#     #     User,
#     #     on_delete=models.CASCADE,
#     #     verbose_name= _("Landlord_of_the_tenant"),
#     #     related_name= "Landlord_of_the_tenant",
#     #     null = True,
#     #     help_text=_(' this provides the landlord details to which this application will be sent to')
#     # )

#     properties = models.ForeignKey(
#         Properties,
#         on_delete=models.CASCADE,
#         verbose_name= _("Properties"),
#         null = True,
#         blank = True,
#         help_text= _("Properties assigned to a tenant."),
#     )

#     full_name = models.CharField(
#         max_length = 250,
#         verbose_name = _('First Name and Last Name'),
#         null = True,
#         blank = True,
#         help_text = _( "This is the tenant full name as it appears in their valid ID" )
#     )

#     date_of_birth = models.CharField(
#         max_length= 100,
#         verbose_name = _("Date of Birth"),
#         null = True,
#         blank = True,
#         help_text= _("This is the tenant date of birth as it is on ID")
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

#     email_address = models.CharField(
#         max_length = 250,
#         verbose_name= _("Email"),
#         blank = True,
#         null = True,
#         help_text = _(" Holds the email address of the tenant")
#     )

#     contact_number = models.CharField(
#         max_length = 100,
#         verbose_name= _("Contact Number"),
#         blank = True,
#         null = True,
#         help_text = _(" Holds tenants contact Number")
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
#         max_length = 100,
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

#     status = models.BooleanField(
#         verbose_name=_("Active"),
#         default=False,
#         null=True,
#         blank=True,
#         help_text=_(" This indicates if the status option type is enabled True or False."),
#     )

    
#     def __str__(self):
#         return str(self.tenant)

#     class Meta:
#         verbose_name = _("Applicant_Information")
#         verbose_name_plural = _("Applicant_Information")






