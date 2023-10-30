from .models import Contact

def baseView(request):
    cont = Contact.objects.all()
    context = {
        "contact": cont,
        "sitename": "Samsung",
    }

    return context