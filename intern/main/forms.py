
from django.forms import widgets
from django.http import request




from .models import *
from django import forms


class Step1Forms(forms.ModelForm):

    class Meta:
        model = Form
        fields = ('name','user','sername','studentID','date','major','company','addresscompany','destination','phone','email') 
        widgets = {'name': forms.TextInput,
        'sername': forms.TextInput,'studentID':forms.TextInput,'date': forms.SelectDateWidget,'major':forms.TextInput,'company':forms.TextInput,'addresscompany':forms.TextInput,
        'destination':forms.TextInput,'phone':forms.TextInput,'email':forms.TextInput}