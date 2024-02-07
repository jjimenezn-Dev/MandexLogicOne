from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Otros campos según sea necesario

    def __str__(self):
        return self.name
