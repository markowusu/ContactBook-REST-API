from django.shortcuts import render
from .models import AddressBook
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializers import AddressBookSerializers
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination



@app_view(['POST'])
def create_contact(request):
    if request.method == 'POST':
        contact_data = JSONParser().parser(request)
        contact_serializer = AddressBookSerializers(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return Response(contact_serializer.data, status= status.HTTP_201_CREATED)
    return Response(contact_serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET', ])
def get_contact_by_id(request, pk ):
    try:
        contact = AddressBook.objects.get(pk=pk)
        
    except AddressBook.DoesNotExist:
        return  Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = AddressBookSerializers(contact)
        return Response(serializer.data, status = status.HTTP_200_OK)



 @app_view(['PUT'])
 def update_contact_by_id(request,pk):
    try:
        contact = AddressBook.objects.get(pk=pk)
    except AddressBook.DoesNotExist():
        return Response("This user does not exit", status=status.HTTP_404_NOT_FOUND)    

    contact_data = JSONParser.parser(request)
    contact_serializer = AddressBookSerializers(contact, data=contact_data)

    if contact_serializer.is_valid():
        contact_serializer.save()
        return Response(contact_serializer.data)
    return Response(contact_serializer.errors, status= status.HTTP_400_BAD_REQUEST)    



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
