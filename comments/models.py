from django.db import models
from properties.models import Properties
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Comments(models.Model):

    properties = models.ForeignKey(
        Properties,
        on_delete= models.CASCADE,
        verbose_name= _("Property Comment"),
        null= True,
        help_text= _("This holds the property the user or visitor is commenting on.")
    )

    comment = models.TextField(
        verbose_name= _("Comment"),
        null = True,
        blank = True,
        help_text= _("This holds the comment made for the property")
    )

    date_time = models.DateTimeField(
        verbose_name=_("Date & Time"),
        auto_now_add= True,
        null=True,
        blank=True,
        help_text=_(" This holds time and the date the comment was made.")
    )


    def __str__(self):
        return str(self.comment)

    class Meta:
        verbose_name = _('All Property Comments')
        verbose_name_plural = _('All Properties Comments')
