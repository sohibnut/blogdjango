from django.shortcuts import render
from .models import Banner, Aboutus, Service, Comment
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
    if about:
        about = about[0]


    services = Service.objects.all().order_by("-time")
    if len(services) > 4:
        services = services[:4]

    comments = Comment.objects.all().order_by("-time")
    if len(comments) > 3:
        services = services[:3]
    

    wser = []
    for x in range(len(services)):
        if x%2==0:
            wser.append([]) 
        wser[-1].append(services[x])

    

    print(wser)            

    context = {
        "bans": bans,
        "about": about,
        "services": wser,
        "comments": comments,
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
    services = Service.objects.all().order_by("-time")


    wser = []
    for x in range(len(services)):
        if x%2==0:
            wser.append([])
        wser[-1].append(services[x])

    context = {
        "services": wser,
    }
    return render(request, 'service.html', context)

def contactPage(request):
    contactForm = ContactForm(request.POST)
    if request.POST and contactForm.is_valid():
        contactForm.save()

    context = {

    }
    return render(request, 'contact.html', context)