from ast import Delete
from email.mime import application
import os
import io
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from matplotlib.style import context
from numpy import full
from .models import *
from django.template.loader import *
from django.db.models import Sum
from django.core.files.storage import *
from django.http import *
from django.shortcuts import render ,get_object_or_404
from shutil import copyfile
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
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

data = {
    "company" : "ptt"
}
from django.template.loader import *
def toPDF(request):
    
    form = get_object_or_404(Form,user=request.user)
    # pattern = get_object_or_404(Form)
    template_path = 'main/toPDF.html'
    context = {'form' : "ANUDCHANA อนุชนา 6210612575 " ,}
    #  'paatern' : pattern} 
    response = HttpResponse(content_type='application/pdf')
    response ['Content-Dinposition'] =  'fliename = "test.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # pdf = render_to_pdf('main/toPDF.html',data)
    # return HttpRequest(pdf , content_type='application/pdf')
    pisa_status = pisa.CreatePDF(
       html.encode("UTF-8"), dest=response )
    if pisa_status.err:
        return HttpResponse('We had some error <pre>'+html+'</pre>')
    return response
# from django.shortcuts import render
# from io import BytesIO
# def render_to_pdf(template_src,context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")),result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(),content_type='application/pdf')
#     return None
