from django.contrib import admin

from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('street', 'city', 'zipcode', 'country')
        }),
    )
    model = Address
