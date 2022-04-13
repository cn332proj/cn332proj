from ctypes import addressof
import email
from django.contrib.auth.models import User
from wsgiref.headers import Headers
from django.db import models
from django.utils import timezone
from matplotlib.pyplot import title

# Create your models here.


class News(models.Model):
    header = models.CharField(max_length=150, null=True,)
    pdf = models.FileField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.header


class Company(models.Model):

    Company = models.CharField(max_length=150, null=True,)
    Description = models.CharField(max_length=150, null=True,)
    Published = models.DateTimeField(default=timezone.now)
    close = models.DateTimeField(default=None)
    link = models.URLField(max_length=200, null=True,)

    def __str__(self):
        return self.Company


class Form(models.Model):
    class title(models.TextChoices):
        miss = "นางสาว"
        mrs = "นาง"
        mr = "นาย"

    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    nameTitle = models.CharField(max_length=100,
                                 choices=title.choices,
                                 default=None,
                                 )
    name = models.CharField(max_length=150, null=True,)
    sername = models.CharField(max_length=150, null=True,)
    studentID = models.CharField(max_length=10, null=True,)
    date = models.DateTimeField(default=timezone.now)
    major = models.CharField(max_length=150, null=True,)
    company = models.CharField(max_length=150, null=True,)
    addresscompany = models.CharField(max_length=150, null=True,)
    destination = models.CharField(max_length=150, null=True,)
    phone = models.CharField(max_length=10, null=True,)
    email = models.CharField(max_length=150, null=True,)

    def __str__(self):
        return self.name


class PDFForm (models.Model):
    header = models.CharField(max_length=150, null=True,)
    body = models.TextField(blank=True)
    link = models.URLField(max_length=200, null=True,)
    logo = models.FileField(blank=True, null=True)
    signature = models.FileField(blank=True, null=True)
    address = models.CharField(max_length=150, null=True,)
    booknumber = models.CharField(max_length=50, null=True,)

    def __str__(self):
        return self.header


class Dowload(models.Model):
    header = models.CharField(max_length=150, null=True,)
    pdf = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.header
