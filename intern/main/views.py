import re
from sys import intern
from turtle import up
from flask_login import logout_user
from platformdirs import user_documents_dir
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from ast import Delete, For
from email.mime import application
import os
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from matplotlib import dates
# from matplotlib.style import context
from numpy import full

from .models import *
from django.template.loader import *
from django.db.models import Sum
from django.core.files.storage import *
from django.http import *
from django.shortcuts import render, get_object_or_404
from shutil import copyfile
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import *
from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.views.generic.edit import CreateView
from .forms import *
from django.urls import reverse_lazy

from django.shortcuts import render,redirect

from . import views
# Create your views here.

from django.contrib.auth.models import User

from .models import *
# Create your views here.
# main


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("user:login"))
    else:
        return render(request, "main/index.html")


def news(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "main/news.html", context)


def company(request):
    company = Company.objects.all()
    context = {"company": company}
    return render(request, "main/companylist.html", context)


def news_content(request, number):
    fs = FileSystemStorage()
    file = (get_object_or_404(News, pk=number)).pdf
    filename = os.path.basename(file.name)

    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename = news.pdf'

            return response
    else:
        return HttpResponseNotFound



# from django.template.loader import *

def Step1toPDF(request):

    buffer = io.BytesIO()
    # ดึงไฟล์ THSarabunNew.ttf มาลงทะเบียนฟอนต์ในโค้ด
    pdfmetrics.registerFont(TTFont('THSarabunIT๙', 'THSarabunIT๙.ttf'))
    form = get_object_or_404(Form, user=request.user)
    c = canvas.Canvas(buffer)  # ไฟล์ที่จะเขียน
    c.setFont("THSarabunIT๙", 14)  # กำหนดฟอนต์ที่ใช้ และขนาดคือ 30
    date = form.date.strftime(" %m/%d/%Y ")
    c.setTitle("แบบฟอร์มขอหนังสือขอความอนุเคราะห์ฝึกงานภาคฤดูร้อน/สหกิจศึกษา")
    # กำหนดพิกัดที่เขียนและข้อความที่เขียน
    c.drawString(
        180, 780, "แบบฟอร์มขอหนังสือ ขอความอนุเคราะห์ฝึกงานภาคฤดูร้อน/สหกิจศึกษา")
    c.drawString(
        190, 750, "**** กรุณาเขียนตัวบรรจง เพื่อความถูกต้องในการพิมพ์หนังสือ ****")
    c.drawString(400, 710, "วันที่ " + date)
    c.drawString(80, 670, "ชื่อนักศึกษา   "+form.nameTitle+form.name +
                 "    "+form.sername + "      เลขทะเบียน     "+form.studentID)
    c.drawString(80, 640, "เป็นนักศึกษา " + form.major)
    c.drawString(
        80, 610, "ชื่อบริษัท (ที่จะไปฝึกงาน/สหกิจกษา) " + form.company)
    c.drawString(80, 580, "ที่อยู่บริษัท (ถ้ามี) " + form.addresscompany)
    c.drawString(
        80, 550, "หนังสือขอความอนุเคราะห์การฝึกงาน/สหกิจศึกษา เรียน (ตําแหน่ง)  " + form.destination)
    c.drawString(80, 520, "เบอร์โทรติดต่อนักศึกษา   " +
                 form.phone + "   E-mail   " + form.email)

    c.showPage()
    c.save()  # บันทึกไฟล์
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='แบบฟอร์มขอหนังสือขอความอนุเคราะห์ฝึกงานภาคฤดูร้อน/สหกิจศึกษา.pdf')

    # pattern = get_object_or_404(Form)
    template_path = 'main/toPDF.html'
    context = {'form': "ANUDCHANA อนุชนา 6210612575 ", }
    #  'paatern' : pattern}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Dinposition'] = 'fliename = "test.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # pdf = render_to_pdf('main/toPDF.html',data)
    # return HttpRequest(pdf , content_type='application/pdf')
    pisa_status = pisa.CreatePDF(
        html.encode("UTF-8"), dest=response)
    if pisa_status.err:
        return HttpResponse('We had some error <pre>'+html+'</pre>')
    return response
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


class Step1Form(CreateView):
    model = Form
    form_class = Step1Forms
    template_name = 'main/step1.html'
    success_url = reverse_lazy('main:Step2')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.booknumber = None
        return super().form_valid(form)

class Step2Form(CreateView):
    pass
    # model = Form
    # form_class = Step1Forms
    # template_name = 'main/start.html'
    # 

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


def Step2toPDF(request):
    
    buffer = io.BytesIO() 
    
    form = get_object_or_404(Form, user=request.user)
    c = canvas.Canvas(buffer)  
    
    logo = ImageReader('logo.png')
    sig = ImageReader('image.png')
    date = form.date
    month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[date.month]
    thai_year = date.year + 543
    pdfmetrics.registerFont(TTFont('THSarabunIT๙', 'THSarabunIT๙.ttf'))
    c.setFont("THSarabunIT๙", 14)  
    c.drawImage(logo,260,730, mask='auto',width=80 ,height=80)
    c.drawImage(sig,295,235, mask='auto',width=130 ,height=40)
    c.drawString(80, 740, "ที่ "+form.booknumber)
    c.drawString(400, 740, "คณะวิศวกรรมศาสตร์")
    c.drawString(400, 720, "มหาวิทยาลัยธรรมศาสตร์ ศูนย์รังสิต")
    c.drawString(400, 700, "อ. คลองหลวง จ. ปทุมธานี ๑๒๑๒๐")
    c.drawString(320, 660, "%d %s %d "%(date.day, month_name, thai_year))
    c.drawString(80, 620, "เรื่อง ขอความอนุเคราะห์นักศึกษาฝึกงานภาคฤดูร้อน")
    c.drawString(80, 590, "เรียน " + form.destination)
    c.drawString(80, 560, "สิ่งที่ส่งมาด้วย แบบตอบรับนักศึกษาฝึกงานภาคฤดูร้อน")
    c.drawString(
        150, 530, "ด้วย ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์   คณะวิศวกรรมศาสตร์   มหาวิทยาลัยธรรมศาสตร์")
    c.drawString(
        80, 510, "ได้กำหนดวิชาการฝึกงานทางวิศวกรรมคอมพิวเตอร์ไว้ในหลักสูตร โดยมีนโยบายที่จะส่งเสริมให้นักศึกษาชั้นปีที่ ๓ ได้มี")
    c.drawString(
        80, 490, "ประสบการณ์และความรอบรู้จากการทำงานจริง ตลอดจนรู้จักใช้ความรู้จากการศึกษามาประยุกต์เข้ากับการทำงาน")
    c.drawString(
        150, 460, "ในการนี้ ภาควิชาฯจึงขอความอนุเคราะห์ให้นักศึกษาดังรายชื่อต่อไปนี้")
    c.drawString(120, 440, form.nameTitle + form.name + "   " +
                 form.sername + "   เลขทะเบียน   " + form.studentID + "   " + form.major)
    c.drawString(
        80, 410, "ได้มีโอกาสเข้าฝึกงานในหน่วยงานของท่าน ช่วงปิดภาคฤดูร้อน ระหว่างวันที่ ๖ มิถุนายน ถึงวันที่ ๓๑ กรกฎาคม ๒๕๖๕")
    c.drawString(
        80, 390, "เป็นเวลาไม่น้อยกว่า   ๖  สัปดาห์ติดต่อกัน  (ไม่น้อยกว่า   ๒๔๐  ชั่วโมง)   ภาควิชาฯ   หวังเป็นอย่างยิ่งว่าจะได้รับความ")
    c.drawString(80, 370, "อนุเคราะห์จากท่าน ในครั้งนี้")
    c.drawString(
        150, 340, "จึงเรียนมาเพื่อโปรดพิจารณาให้ความอนุเคราะห์ด้วย   จักขอบพระคุณยิ่ง")
    c.drawString(320, 310, "ขอแสดงความนับถือ")
    c.drawString(280, 210, "(ผู้ช่วยศาสตราจารย์ ดร.พิศาล แก้วประภา)")
    c.drawString(275, 190, "หัวหน้าภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์")
    c.drawString(80, 100, "ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์")
    c.drawString(80, 80, "โทร. ๐ ๒๕๖๔ ๓๐๐๑ - ๙ ต่อ ๓๐๓๗")
    c.drawString(80, 60, "อีเมล ece@engr.tu.ac.th")

    c.showPage()
    c.save()  # บันทึกไฟล์
    buffer.seek(0)
    # ,as_attachment=True
    return FileResponse(buffer, filename='หนังสือขอความอนุเคราะห์ฝึกงานภาคฤดูร้อน/สหกิจศึกษา.pdf')

# class Step2Form(CreateView):
#     model = Form
#     form_class = Step2Forms
#     template_name = 'main/step2_Admin.html'
#     success_url = reverse_lazy('main:Step2')

#     def form_valid(self, form):
#         return super().form_valid(form)
from .forms import Step2Forms

def step2A(request,pk):
    Book = Form.objects.get(id=pk)
    context = {'Book':Book} 
    if 'Book' not in request.POST:
        return render(request,'main/step2_Admin.html',context)
        # return render(request, "main/step2_Admin.html")
    else:
        booknumber = request.POST.get('Book',None)
        Book.booknumber = booknumber
        Book.save()
        return redirect('/main/Step2')
        # return render(request, "main:index")
    

def step2U(request):
    user = request.user.is_superuser
    if not user:
        form = Form.objects.get(user_id=request.user)
    else:
        form = Form.objects.all()
    context = {"form": form,}
    return render(request, "main/step2.html", context)

def step3 (request):
    files = Documentstep3.objects.all()
    if request.method == 'POST':
        form = Step3Forms(request.POST, request.FILES)
        filename = form['filename'].value()
        
        if form.is_valid():
            form.save()
			# eachsubject(request, form['subjectid'].value())
            return redirect('Step3')
        else:
            print(form.errors)
    else:
        form = Step3Forms()
        return render(request, 'main/step3.html', {
        'form': form,
        'files' : files
    })

    return render(request, "main/step3.html")

def step4(request):
    files = Documentstep4.objects.all()
    if request.method == 'POST':
        form = Step4Forms(request.POST, request.FILES)
        filename = form['filename'].value()

        if form.is_valid():
            form.save()
            # eachsubject(request, form['subjectid'].value())
            return redirect('main:Step5')
        else:
            print(form.errors)
    else:
        form = Step4Forms()
        return render(request, 'main/step4.html', {
            'form': form,
            'files': files
        })

    return redirect('main:Step5')

def step5 (request):
    files = Documentstep5.objects.all()
    if request.method == 'POST':
        form = Step3Forms(request.POST, request.FILES)
        filename = form['filename'].value()
        
        if form.is_valid():
            form.save()
			# eachsubject(request, form['subjectid'].value())
            return redirect('Step5')
        else:
            print(form.errors)
    else:
        form = Step3Forms()
        return render(request, 'main/step5.html', {
        'form': form,
        'files' : files
    })

    return render(request, "main/step3.html")