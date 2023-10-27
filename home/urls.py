from django.urls import path
from .views import homePage, aboutPage, contactPage, servicePage

urlpatterns = [
    path('', homePage, name="home"),
    path('about/', aboutPage, name="about"),
    path('service/', servicePage, name="service"),
    path('contact/', contactPage, name="contact"),
]