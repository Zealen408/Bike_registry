from django.contrib import admin
from .models import bike
# Register your models here.


class BikeAdmin(admin.ModelAdmin):
    list_display = ['bike_serial_number', 'owner', 'bike_stolen']
    list_editable = ['bike_stolen']


admin.site.register(bike, BikeAdmin)
