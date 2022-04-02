from ast import Delete
from email.mime import application
import os
import io
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from numpy import full
from .models import *
from django.template.loader import *
from django.db.models import Sum
from django.core.files.storage import *
from django.http import *
from django.shortcuts import render ,get_object_or_404
from shutil import copyfile
from reportlab.pdfgen import canvas
# Create your views here.
# main

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user:login"))
    else:
        return render(request, "main/index.html")

def start(request):
    return render(request, "main/step1.html")

def news(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "main/news.html", context)

def company(request):
    company = Company.objects.all()
    context = {"company": company}
    return render(request, "main/companylist.html", context)

def news_content(request, number):
    fs= FileSystemStorage()
    file = (get_object_or_404(News,pk = number)).pdf
    filename = os.path.basename(file.name)

    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename = news.pdf'
                
            return response
    else:
        return HttpResponseNotFound


       
def step1_1(request):
    file_path = "temp/"
    if request.method == 'POST' and request.FILES['file1']:
            file1 = request.FILES['file1']
            fs = FileSystemStorage()
            name = "test_" + request.user.username + ".pdf"

            if os.path.isfile("file/" + file_path + name):
                os.remove("file/" + file_path + name)

            filename = fs.save(file_path + name , file1)
            uploaded_file_url = fs.url(filename)
            #_name = name

            copyfile("file/" + file_path + name, "static/file/test/" + name)
            os.remove("file/" + file_path + name)    
    return render(request, "main/success.html")

def toPDF(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(50,700,"test")
    p.drawString(50,600,"to PDF")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='แบบตอบรับนักศึกษาฝึกงานภาคฤดูร้อน.pdf')