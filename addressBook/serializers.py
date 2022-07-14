from rest_framework import serializers
from .models import AddressBook

class AddressBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = AddressBook
        fields = [
            "pk",
            "first_name",
            "last_name",
            "date_added",
            "phone_number"

        ]