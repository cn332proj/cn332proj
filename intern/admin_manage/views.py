from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User,auth
import csv
from user.models import Student
import codecs
# Create your views here.


def add_student(request):
    return render(request, "admin_manage/add_student.html")

def add_student2(request):
	row_stid=int(request.POST.get('column', ''));
	if request.method == 'POST' and request.FILES['sheet']:
			mysheet = request.FILES['sheet']

	csvreader = csv.reader(codecs.iterdecode(mysheet,'utf-8'))
	record = []

	for row in csvreader:
		if row[row_stid-1].isdigit():
			add_user = User.objects.create_user(
	            username = row[row_stid-1],
	            password = row[row_stid-1],
	            email = 'email@mail.com',
	            first_name = "name",
	            last_name = "sur",            
	            )
			add_user.save()
	messages.info(request,'add new student success!')

	return redirect("/admin_manage/add_student")

	
def admin_dashboard(request):
    return render(request, "admin_manage/admin_dashboard.html")