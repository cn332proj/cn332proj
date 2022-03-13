from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.views import *
from django.contrib.auth.forms import *
from django.shortcuts import render ,get_object_or_404
from django.urls import reverse

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/editpassword.html'

class CustomUserChangeView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/editProfile.html'
    def get_object(self):
        return self.request.user

# def index(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse("users:login"))
#     else:
#         get_subject = request.user.students.all()
#         return render(request, "users/index.html",{
#         "subject":get_subject,
#     })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            messages.warning(request, "Invalid credential.")
            return render(request, "users/login.html", {
                "messages": messages.get_messages(request)
            })


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out.")
    return render(request, "users/login.html", {
        "messages": messages.get_messages(request)
    })