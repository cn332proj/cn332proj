
from django.forms import widgets
from django.http import request
from .models import *
from django import forms


class Step1Forms(forms.ModelForm):
    class Meta:
        model = Form
        fields = ('nameTitle', 'name', 'sername', 'studentID', 'date', 'major',
                  'company', 'addresscompany', 'destination', 'phone', 'email')
        widgets = {'name': forms.TextInput,
                   'sername': forms.TextInput, 'studentID': forms.TextInput, 'date': forms.SelectDateWidget, 'major': forms.TextInput, 'company': forms.TextInput, 'addresscompany': forms.TextInput,
                   'destination': forms.TextInput, 'phone': forms.TextInput, 'email': forms.TextInput, }


class Step2Forms(forms.ModelForm):
    class Meta:
        model = Form
        fields = ('booknumber',)
        widgets = {'booknumber': forms.TextInput}


class Step3Forms(forms.ModelForm):
    class Meta:
        model = Documentstep3
        fields = ('filename', 'attachment')

    def __init__(self, *args, **kwargs):
        super(Step3Forms, self).__init__(*args, **kwargs)

        self.fields['filename'].widget.attrs.update(style='max-width: 50em')


class Step5Forms(forms.ModelForm):
    class Meta:
        model = Documentstep5
        fields = ('filename', 'attachment')

    def __init__(self, *args, **kwargs):
        super(Step5Forms, self).__init__(*args, **kwargs)

        self.fields['filename'].widget.attrs.update(style='max-width: 50em')
