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
        User, on_delete=models.CASCADE,
        verbose_name= _("Tenant"),
        related_name= "Tenant",
        null = True,
        help_text=_(' this provides the recipients to which this message will be sent to')
    )

    landlord = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name= _("Landlord"),
        related_name= "Landlord_properties",
        null = True,
        help_text=_(' this provides the recipients to which this message will be sent to')
    )

    properties = models.ForeignKey(
        Properties, on_delete=models.CASCADE,
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
        help_text= _("This is the date when the action was taken."),
    )

    notification = models.BooleanField(
        verbose_name= _("Notification"),
        default= False,
        null= True,
        blank= True,
        help_text= _("This indicates if the notification option type is enabled True or False."),

    )
    
    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Tenant")
        verbose_name_plural = _("Tenants")

    def __str__(self):
        return str(self.Tenant.Properties)



    """
    properties_action = rented , processing , declined , review

    action --- model choice-properties_action
    status --- model boolean
    action_date --- model datetime
    optional - notification --- model boolean-false if the action is rented ... its going to push an email notification to the tenant

    # property_price = Tenant.objects.filter( user = request.user )
    # for p in property_price:
    #     print(p.properties.price)

    # load humanize
    # {% for p in  property_price %}
    #     {{ p.properties.price | intcomma }} #20,000.00
    # {% endfor  %}



    """
