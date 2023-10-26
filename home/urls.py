from django.urls import path
from .views import homePage

urlpatterns = [
    path('', homePage, name="home"),
    path('about/', homePage, name="about"),
    path('services/', homePage, name="services"),
    path('contact/', homePage, name="contact"),
]