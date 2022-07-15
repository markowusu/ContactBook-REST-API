from rest_framework import serializers
from .models import AddressBook, File 

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



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model= File
        fields =["file", "description", "timestamp"]   


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField() 


class SaveFileSerializer(serializers.Serializer):
    class Meta:
        model = AddressBook
        fields = [
            "first_name",
            "last_name",
            "date_added",
            "phone_number"
        ]
        