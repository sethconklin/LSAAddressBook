from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=40)
    email_address = models.CharField(max_length=50)
    street_address = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name + " " + self.last_name