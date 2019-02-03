from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    first_name = models.CharField(max_length=20)
    family_name = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    company = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17)

    def __str__(self):
        return self.first_name
