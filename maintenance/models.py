from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _

# Custom Apps 
from helpers.common.basemodel import BaseModel
from estate_project.users.models import User



MAINTENANCE_ACTION = (

        ("reported", _("Reported")),
        ("assigned", _("Assigned")),
        ("in progress", _("In Progress")),
        ("completed", _("Completed")),
        
    )


class Maintenance ( BaseModel ):

    """
    This holds the maintenance informationand progress of the property between tenant and landlord.
    """

    tenant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name= _("Tenant"),
        related_name= "Tenant_User",
        null = True,
        help_text=_(' this provides the sender who is sending the message')
    )

    # landlord = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     verbose_name= _("Landlord"),
    #     related_name= "Landlord_User",
    #     null = True,
    #     help_text=_(' this provides the recipients to which this message will be sent to')
    # )

    maintenance_type = models.CharField(
        max_length= 100,
        verbose_name= _("Type"),
        null= True,
        blank= True,
        help_text= _("The type of maintainance issue."),
    )

    issue = models.CharField(
        max_length= 100,
        verbose_name= _("Issues"),
        null= True,
        blank= True,
        help_text= _("The isssue to be reported."),
    )

    description = models.TextField(
        max_length= 100,
        verbose_name= _("Description"),
        null= True,
        blank= True,
        help_text= _("The size of the family of the tenant."),
    )

    action = models.CharField(
        choices= MAINTENANCE_ACTION,
        verbose_name= _("Action"),
        max_length= 20,
        null= True,
        blank= True,
        help_text= _("This is the action to take place when applying for maintenance."),
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

    def __str__(self):
        return str(self.issue)

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Maintenance")
        verbose_name_plural = _("Maintenance")


