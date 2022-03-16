from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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
    news = New.objects.all()
    context = {"news": news}
    return render(request, "doctors/news.html", context)

def news_content(request, pk):
    new = New.objects.filter(id=pk).first()
    context = {"new": new}
    return render(request, "doctors/news_one.html", context)
            