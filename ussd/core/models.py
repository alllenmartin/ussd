from django.db import models


class Savings(models.Model):
    phone_number=models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
