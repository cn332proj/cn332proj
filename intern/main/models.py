from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    header = models.CharField(max_length=150, null = True,)
    pdf = models.FileField(blank=True,null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.header

class Company(models.Model):

    Company	= models.CharField(max_length=150, null = True,)
    Description = models.CharField(max_length=150, null = True,)
    Published = models.DateTimeField(default=timezone.now)
    close = models.DateTimeField(default=None)
    link = models.URLField(max_length=200,null = True,)

    def __str__(self):
        return self.Company