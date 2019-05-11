import uuid
from django.db import models


class Setting(models.Model):
    title = models.CharField(max_length=50,help_text='Title displayed on home page')
    navbar_brand = models.ImageField(upload_to = "homepage",default="img/homepage/logo.png")
    background_image = models.ImageField(upload_to = "homepage",default="img/homepage/logo.png")
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Request(models.Model):
    contact_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, help_text="Name of user who supplied request")
    email = models.EmailField(help_text="Contact details of contacter")
    subject = models.CharField(max_length=50, help_text="subject matter of message")
    message = models.TextField(help_text="message")

    def __str__(self):
        return self.name