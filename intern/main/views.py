from ast import Delete
from email.mime import application
import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.template.loader import *
from django.db.models import Sum
from django.core.files.storage import *
from django.http import *
from django.shortcuts import render ,get_object_or_404
# Create your views here.
# main

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user:login"))
    else:
        return render(request, "main/index.html")

def start(request):
    return render(request, "main/start.html")

def news(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "doctors/news.html", context)

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