from django.shortcuts import render
from .models import AddressBook
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.decorators import api_view
from.addressBookSerializers import AddressBookSerializers, FileSerializer, FileUploadSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
import csv, io
import pandas as pd 


@api_view(['GET','POST'])
def create_contact(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 20
        contacts = AddressBook.objects.all()
        result_page = paginator.paginate_queryset(contacts, request)
        serializer = AddressBookSerializers(contacts, many=True)
        return paginator.get_paginated_response(serializer.data)
        

    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
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
        return Response(serializer.data, status = status.HTTP_201_CREATED)



@api_view(['PUT'])
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
        return Response("This user does not exist", status= status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        count = delete_operation = contact.delete()
    data ={}
    if delete_operation:
        data["success"] = "{} items deleted successfuly".format(count[0])
    else: 
        data["failure"] = "delete failed"

    return Response(data= data)        
                    



class AddressBookList(generics.ListAPIView):
    queryset = AddressBook.objects.all()
    serializer_class  = AddressBookSerializers
    pagination_class = PageNumberPagination


class FileView(generics.CreateAPIView):
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception = True)

        file = serializer.validated_data['file']
        reader = pd.read_csv(file)

        for _, row in reader.iterrows():
            new_file = AddressBook(
                first_name = row["first_name"],
            last_name= row["last_name"],
           date_added = row["date_added"],
            phone_number= row["phone_number"]
            )
        new_file.save()   

        return Response({"status": "success"},status= status.HTTP_201_CREATED) 
