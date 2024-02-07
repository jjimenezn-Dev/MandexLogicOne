from django.db import models
from clients.models import Client
from delivers.models import Deliver

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    clients = models.ManyToManyField(Client)
    delivers = models.ManyToManyField(Deliver)

    def __str__(self):
        return self.name
