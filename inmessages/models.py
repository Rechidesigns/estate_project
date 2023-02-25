# Django import 
from django.db import models
from django.utils.translation import gettext_lazy as _

# Custom Apps 
from helpers.common.basemodel import BaseModel
from estate_project.users.models import User


class Esate_Messages ( BaseModel ):
    """
    this hold the messaging system btw the landlord and 
    the tenants
    """

    message_type  = models.CharField(
        verbose_name= _('Message Type'),
        max_length= 255,
        null = True,
        blank= True,
        help_text=_("this fields requires the message type of which the message will be sent with and categorized into")
    )

    recipients = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        verbose_name = _('Message Recipient'),
        related_name = "message_recipients",
        null = True,
        help_text=_(' this provides the recipients to which this message will be sent to')
    )

    subject  = models.CharField(
        verbose_name= _('Subject'),
        max_length= 255,
        null = True,
        blank= True,
        help_text=_(" The subject line of an email is the single line of text people see when they receive your email. This one line of text can often determine whether an email is opened or sent straight to the trash, so make sure it's optimized for your audience ")
    )

    body = models.TextField(
        verbose_name= _('Subject'),
        null = True,
        blank= True,
        help_text= _(" The body is the actual text of the email. Generally, you'll write this just like a normal letter, with a greeting, one or more paragraphs, and a closing with your name. ")
    )

    active = models.BooleanField(
        verbose_name=_("Active"),
        default=False,
        null=True,
        blank=True,
        help_text=_(" this indicates is the active messages is enabled or not ")
    )

    def __str__(self):
        return str(self.recipients)

    class Meta:
        ordering = ('-created_date',)
        verbose_name = _("Messages")
        verbose_name_plural = _("Messages")


