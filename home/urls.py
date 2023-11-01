from django.urls import path
from .views import homePage, aboutPage, contactPage, servicePage, serviceDetailPage 

urlpatterns = [
    path('', homePage, name="home"),
    path('about/', aboutPage, name="about"),
    path('service/', servicePage, name="service"),
    path('service/<int:id>/', serviceDetailPage, name="detail"),
    path('contact/', contactPage, name="contact"),
]