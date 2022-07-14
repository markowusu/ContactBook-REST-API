from django.shortcuts import render
from .models import AddressBook
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AddressBookSerializers
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
@app_view(['POST'])
def create_contact(request):
    if request.method == 'POST':
        serializer = AddressBookSerializers(request.data)





@api_view(['GET', ])
def get_contact_by_id(request, pk ):
    try:
        contact = AddressBook.objects.get(pk=pk)
        
    except AddressBook.DoesNotExist:
        return  Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = AddressBookSerializers(contact)
        return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_contact_by_id(request, pk):
    try:
        contact = AddressBook.objects.get(pk =pk)
    except AddressBook.DoesNotExist:
        return Response("This user id does not exist", status= status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        delete_operation = contact.delete()
    data ={}
    if delete_operation:
        data["success"] = "delete successful"
    else: 
        data["failure"] = "delete failed"

    return Response(data= data)        
                    



class AddressBookList(generics.ListAPIView):
    queryset = AddressBook.objects.all()
    serializer_class  = AddressBookSerializers
    pagination_class = PageNumberPagination



# class AddressBookDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AddressBook.objects.all()
#     serializer_class  = AddressBookSerializers
