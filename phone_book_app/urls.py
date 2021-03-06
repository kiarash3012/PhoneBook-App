from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_contact', views.add_contact, name='add_contact'),
    path('edit_contact/<list_id>', views.edit_contact, name='edit_contact'),
    path('delete_contact/<list_id>', views.delete_contact, name='delete_contact'),
]
