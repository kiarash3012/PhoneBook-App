from django.shortcuts import render, redirect
from .models import Contact


def home(request):
    all_contacts = Contact.objects.all
    return render(request, 'home.html', {'all_contacts': all_contacts})


def add_contact(request):
    return render(request, 'add_contact.html', {})

