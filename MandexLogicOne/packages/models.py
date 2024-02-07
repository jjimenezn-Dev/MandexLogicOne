from django.db import models
from clients.models import Client
from employees.models import Employee
from delivers.models import Deliver

class Package(models.Model):
    description = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    deliver = models.ForeignKey(Deliver, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
