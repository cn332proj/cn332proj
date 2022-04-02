from django.db import models


class Student(models.Model):
	Student_pk = models.BigAutoField(auto_created=True, primary_key=True)
	Student_id = models.CharField(max_length=20 ,null=True)
	Student_prefix = models.CharField(max_length=5 ,null=True)
	Student_name_th = models.CharField(max_length=200 ,null=True)
	Student_name_en = models.CharField(max_length=200 ,null=True)
	Student_email = models.CharField(max_length=200 ,null=True)
	Student_faculty = models.CharField(max_length=200 ,null=True)
	Student_department = models.CharField(max_length=200 ,null=True)
	Student_step = models.IntegerField(default = 0 ,null=True)
# Create your models here.
