from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .models import User
# from estate_project.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()

@admin.register( User )
class UserAdmin (admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email')
    list_display_links = ( 'first_name', 'last_name','email')

