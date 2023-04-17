from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class InmessagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "inmessages"
    verbose_name = _(" Inmessages ")
