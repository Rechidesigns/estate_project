from django.contrib import admin

from .models import Properties , Other_Amenities , OutDoor_Spaces , Utilities , Parking_Type , Property_Type, Appliances
from .models import Comments
# Register your models here.

@admin.register( Properties )
class PropertiesAdmin (admin.ModelAdmin):
    list_display = ('landlord' , 'address_1' , 'created_date' , 'modified_date')
    list_display_links = ('landlord' , 'address_1' )


@admin.register( Other_Amenities )
class Other_AmenitiesAdmin (admin.ModelAdmin):
    list_display = ('option', 'active')
    list_display_links = ('option', 'active')


@admin.register( OutDoor_Spaces )
class OutDoor_SpacesAdmin (admin.ModelAdmin):
    list_display = ('option', 'active')
    list_display_links = ('option', 'active')


@admin.register( Utilities )
class UtilitiesAdmin (admin.ModelAdmin):
    list_display = ('option', 'active')
    list_display_links = ('option', 'active')


@admin.register( Parking_Type )
class Parking_TypeAdmin (admin.ModelAdmin):
    list_display = ('option', 'active')
    list_display_links = ('option', 'active')


@admin.register( Property_Type )
class Property_TypeAdmin (admin.ModelAdmin):
    list_display = ('option', 'active')
    list_display_links = ('option', 'active')


@admin.register( Appliances )
class AppliancesAdmin (admin.ModelAdmin):
    list_display = ('option', 'active')
    list_display_links = ('option', 'active')


@admin.register( Comments )
class CommentsAdmin (admin.ModelAdmin):
    list_display = ('property','comment', 'active') 
    list_display_links = ('property', 'active')