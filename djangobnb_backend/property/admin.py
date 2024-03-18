from django.contrib import admin

from .models import Property, Reservation


admin.site.register(Property)
admin.site.register(Reservation)