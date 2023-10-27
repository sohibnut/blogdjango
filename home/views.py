from django.shortcuts import render
from .models import Banner, Aboutus
from .forms import ContactForm

# Create your views here.
def homePage(request):
    contactForm = ContactForm(request.POST)
    if request.POST and contactForm.is_valid():
        contactForm.save()


    bans = Banner.objects.all().order_by("-publish_time")
    elements = 3
    if len(bans) > elements:
        bans = bans[:elements]


    about = Aboutus.objects.all().order_by("-time")
    about = about[0]



    context = {
        "bans": bans,
        "about": about,

    }
    return render(request, 'index.html', context)

def aboutPage(request):
    elements = 10
    abouts = Aboutus.objects.all().order_by("-time")
    if len(abouts) > elements:
        abouts = abouts[:elements]

    context = {
        "abouts": abouts
    }
    return render(request, 'about.html', context)

def servicePage(request):
    context = {

    }
    return render(request, 'service.html', context)

def contactPage(request):
    context = {

    }
    return render(request, 'contact.html', context)