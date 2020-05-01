from django.contrib import admin

# Register your models here.
from .models import Reservation

#register Reservation model to be edited in admin console
admin.site.register(Reservation)