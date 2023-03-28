from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChangePasswordConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Change_password"
    verbose_name = _("Change Password")
