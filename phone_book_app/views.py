from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


def home(request):
    all_contacts = Contact.objects.all
    return render(request, 'home.html', {'all_contacts': all_contacts})


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Contact Has Been Added'))
            return redirect('home')
        else:
            messages.success(request, ('Seems Like There was An Error...'))
            return render(request, 'add_contact.html', {})
    else:
        return render(request, 'add_contact.html', {})


def edit_contact(request, list_id):
    if request.method == 'POST':
        current_contact = Contact.objects.get(pk=list_id)
        form = ContactForm(request.POST or None, instance=current_contact)
        if form.is_valid():
            form.save()
            messages.success(request, ('Contact Has Been Edited'))
            return redirect('home')
        else:
            messages.success(request, ('Seems Like There was An Error...'))
            return render(request, 'edit.html', {})
    else:
        get_address = Contact.objects.get(pk=list_id)
        return render(request, 'edit.html', {'get_address': get_address})


def delete_contact(request, list_id):
    if request.method == 'POST':
        current_contact = Contact.objects.get(pk=list_id)
        form = ContactForm(request.POST or None, instance=current_contact)
        if form.is_valid():
            form.save()
            messages.success(request, ('Contact Has Been Deleted'))
            return redirect('home')
        else:
            messages.success(request, ('Seems Like There was An Error...'))
            return render(request, 'delete.html', {})
    else:
        get_address = Contact.objects.get(pk=list_id)
        return render(request, 'delete.html', {'get_address': get_address})
