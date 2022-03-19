from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import requests
import pandas as pd
# Create your views here.


#news
# def news(request):
#     news = News.objects.all()
#     context = {"news": news}
#     return render(request, "doctors/news.html", context)


# login

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser :
            login(request, user)
            return redirect(reverse("admin_manage:admin_dashboard"))
        else:
            login_status = login_api(username,password)
            if  login_status == 200:
                user = authenticate(request, username=username, password=username)
                if user is not None:
                    login(request, user)
                    return redirect(reverse("main:index"))

            else:
                messages.info(request, "invalid Student ID or password")
    return render(request, 'user/login.html')
    
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return render(request, "user/login.html", {
        "messages": messages.get_messages(request)
    })




### login with tu api
def login_api(username,password):
    header = {
        'Content-Type': 'application/json',
        'Application-Key': 'TUdad3354636aacf9e1e7f8954bef241f8dd654708036bf06bf8ae703785b21bc985327cf4b0059571504984688553db30'
    }

    body = {"UserName" : username,"PassWord" : password}

    res = requests.post("https://restapi.tu.ac.th/api/v1/auth/Ad/verify", headers= header, json= body)

    return res.status_code