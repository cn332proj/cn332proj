from django.db import models


class Student(models.Model):
	no = models.BigAutoField(auto_created=True, primary_key=True)
	Student_ID = models.CharField(max_length=200 ,null=True)
	Student_password = models.CharField(max_length=200 ,null=True)
	step = models.IntegerField(default=0)

# Create your models here.
