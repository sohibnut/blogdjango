from django.db import models

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    body = models.CharField(max_length=255)
    publish_time = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email
    

class Aboutus(models.Model):
    title = models.CharField(default="About Us", max_length=30)
    body = models.TextField()
    url = models.URLField()
    button_label = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self) -> str:
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    time = models.DateTimeField(auto_now=True)
    icon = models.ImageField(upload_to="images/", blank=True)

    def __str__(self) -> str:
        return self.title