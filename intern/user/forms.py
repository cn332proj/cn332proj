from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    
    first_name = forms.CharField(label = "First name",)
    last_name = forms.CharField(label = "Last name")
    
    class Meta:
        model = User
        fields = ('username', 'email' ,'first_name','last_name')
  
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username','email' ,'first_name','last_name')
