from django.contrib import admin

# Register your models here.
from .models import AddressBook

admin.site.register(AddressBook)