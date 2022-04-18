
from django.forms import widgets
from django.http import request




from .models import *
from django import forms


class Step1Forms(forms.ModelForm):

    class Meta:
        model = Form
        fields = ('nameTitle','name','sername','studentID','date','major','company','addresscompany','destination','phone','email') 
        widgets = {'name': forms.TextInput,
        'sername': forms.TextInput,'studentID':forms.TextInput,'date': forms.SelectDateWidget,'major':forms.TextInput,'company':forms.TextInput,'addresscompany':forms.TextInput,
        'destination':forms.TextInput,'phone':forms.TextInput,'email':forms.TextInput}

class Step2Forms(forms.ModelForm):

    class Meta:
        model = PDFForm
        fields = ('booknumber',) 
        widgets = {'booknumber':forms.TextInput}