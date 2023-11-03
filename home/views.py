from django.shortcuts import render, redirect
from .models import Banner, Aboutus, Service, Comment
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def redPage(request):
    return redirect('home/')

def homePage(request):
    a = contactPage(request)
      

    bans = Banner.objects.all().order_by("-publish_time")
    ban_elements = 3 # count of elements to show in banner
    if len(bans) > ban_elements:
        bans = bans[:ban_elements]


    about = Aboutus.objects.all().order_by("-time")
    about = about[0] # we get just last published about article


    services = Service.objects.all().order_by("-time")
    ser_elements = 4 # count of elements to show in service section
    if len(services) > ser_elements:
        services = services[:ser_elements]
    wser = []
    for x in range(len(services)):
        if x%2==0:
            wser.append([]) 
        wser[-1].append(services[x])


    comments = Comment.objects.all().order_by("-time")
    com_elements = 5 # count of comments to show
    if len(comments) > com_elements:
        comments = comments[:com_elements]
    comments_id = range(len(comments)) 

    context = {
        "bans": bans,
        "about": about,
        "services": wser,
        "comments": comments,
        "comments_id": comments_id,
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
    elements = 10
    if len(services) > elements:
        services = services[:elements]

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
    if request.POST:
        if contactForm.is_valid():
            contactForm.save()
        else:
            print(contactForm.errors)
            messages.error(request, contactForm.errors)
       

    context = {

    }
    return render(request, 'contact.html', context)

def serviceDetailPage(request, id: int):
    data = Service.objects.get(id=id)
    context = {
        "ser": data,
    }
    return render(request, "service_det.html", context)