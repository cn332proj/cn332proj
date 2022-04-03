from django.urls import path
from . import views
from .views import *
app_name="main"

urlpatterns = [
    path("", views.index, name="index"),
    path("start/", views.start, name="start"),     
    path("step1_1/", views.step1_1, name="step1_1"), 

    #ข่าว
    path('news', views.news, name="news"),
    path('news/<int:number>', views.news_content, name="news_content"),

    #บริษัท
    path('CompanyList', views.company, name="company"),
    path('start', Step1Form.as_view(), name="Step1Form"),
    path('Step1', views.Step1toPDF, name="Step1"),
    path('Step2', views.Step2toPDF, name="Step2"),
]
   