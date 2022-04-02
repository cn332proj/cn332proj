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



class Document(models.Model):
    Document_ID = models.BigAutoField(auto_created=True, primary_key=True)
    Document_student_id = models.CharField(max_length=20 ,null=True)
    Document_file1_id = models.CharField(max_length=200 ,null=True)
    Document_file2_id = models.CharField(max_length=200 ,null=True)
    Document_file3_id = models.CharField(max_length=200 ,null=True)
  


class File1(models.Model):
    File1_ID = models.BigAutoField(auto_created=True, primary_key=True)
    File1_name = models.CharField(max_length=200 ,null=True)
    File1_history_id = models.CharField(max_length=200 ,null=True)
    File1_date = models.DateTimeField(default=timezone.now)
  


class History(models.Model):
    History_ID = models.BigAutoField(auto_created=True, primary_key=True)
    History_student_id = models.CharField(max_length=20 ,null=True)
    History_file_id = models.CharField(max_length=200 ,null=True)
    History_admin_id = models.CharField(max_length=200 ,null=True)
    History_file_type = models.CharField(max_length=1 ,null=True)
    History_date = models.DateTimeField(default=timezone.now)
  