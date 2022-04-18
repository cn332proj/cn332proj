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

    
    path('CompanyList', views.company, name="company"),
    path('Step1', Step1Form.as_view(), name="Step1"),
    path('Step2', Step2Form.as_view(), name="Step2"),
    path('Step1toPDF', views.Step1toPDF, name="Step1toPDF"),
    path('Step2toPDF', views.Step2toPDF, name="Step2toPDF"),
]
   