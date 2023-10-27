from .models import Contact
from django.shortcuts import render

def baseView(request):
    cont = Contact.objects.all()
    context = {
        "contact": cont,
    }

    return context