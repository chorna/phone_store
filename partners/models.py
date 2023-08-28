from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=255)
    ruc = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    is_client = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)

    def __str__(self):
        return self.name
