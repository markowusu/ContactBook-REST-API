from django.urls import path 
from . import views 


urlpatterns = [
    # path("contacts/", views.AddressBookList.as_view()),
    path("contacts/", views.create_contact),
    path("contacts/<int:pk>", views.get_contact_by_id),
    path("contacts/<int:pk>", views.delete_contact_by_id),
    path('contacts/upload-csv/', views.FileView.as_view(), name="file-upload")
]