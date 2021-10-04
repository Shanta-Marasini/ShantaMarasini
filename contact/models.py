from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email_address = models.EmailField(max_length=150)
    message = models.TextField()