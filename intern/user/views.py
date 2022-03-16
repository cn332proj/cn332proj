from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

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
        if user is not None:
            login(request, user)
            return redirect(reverse("main:index"))
        else:
             messages.info(request, 'Username or Password is invalid')
    return render(request, 'user/login.html')
    
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return render(request, "user/login.html", {
        "messages": messages.get_messages(request)
    })