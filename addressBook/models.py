from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class AddressBook(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length = 255)
    phone_number = PhoneNumberField(blank=False, unique= True, null = False)
    date_added = models.DateField(auto_now_add =True)

    def __str__(self):
        return self.phone_number
