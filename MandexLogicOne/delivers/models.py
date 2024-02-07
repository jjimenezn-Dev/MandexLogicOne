from django.db import models
from address.models import Address
from packages.models import Package

class Deliver(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    addresses = models.ManyToManyField(Address)
    packages = models.ManyToManyField(Package)

    def __str__(self):
        return self.name
