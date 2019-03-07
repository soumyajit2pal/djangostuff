from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.

class reminder(models.Model):
    name=models.CharField(max_length=64)
    purpose=models.CharField(max_length=100)
    dosage=models.IntegerField()
    date=models.DateField(default=date.today)
    time=models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name