from django.db import models

# Create your models here.

class Users(models.Model):
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    email=models.EmailField(max_length=256, unique=True)

    def __str__(self):
        return self.first_name
        