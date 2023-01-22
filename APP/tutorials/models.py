from django.db import models

# Create your models here.
class Tutorial(models.Model):
    item = models.CharField(max_length=70, blank=False, default='')
    date = models.CharField(max_length=200, blank=False, default='')
    condition = models.CharField(max_length=2, blank=True, null=True)
    msrp = models.PositiveIntegerField()
    asking_price = models.PositiveIntegerField()