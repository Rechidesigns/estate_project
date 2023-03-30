from datetime import timedelta, datetime
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class OTP(models.Model):
    otp_pin = models.CharField(
        max_length = 6,
        verbose_name = _("OTP"),
        null = True,
        help_text = _(" otp of the user "),
    )

    email = models.EmailField(
        verbose_name = _(" OTP "),
        null = True,
        help_text= _("Email address of the user"),
    )

    pin_duration = models.DateTimeField(
        verbose_name = _("OTP Pin duration"),
        default = timezone.now,
        null= True,
        help_text = _("this holds the duration of pin sent to the user"),
    )

    active = models.BooleanField(
        verbose_name = _("Active"),
        default= True,
        null = True,
        help_text = _("this is the users otp status if active of not"),
    )

    def __str__(self):
        return str(self.email)
    
    def save(self, *args, **kwargs):
        self.pin_duration += timedelta(minutes = 5)
        super(OTP, self).save(*args, **kwargs)

