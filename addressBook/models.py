from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save


class AddressBook(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length = 255)
    phone_number = PhoneNumberField(blank=False, unique= True, null = False)
    date_added = models.DateField(auto_now_add =True)

    def __str__(self):
        return self.phone_number

class File(models.Model):
    file = models.FileField(blank=False, null = False)
    description = models.CharField(max_length = 100)
    timestamp = models.DateField(auto_now_add = True)
    email = models.EmailField(blank=False, null = False)

    def __str__(self):
        return self.file
