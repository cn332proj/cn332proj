from django.urls import path
from . import views
from .views import *
app_name="main"

urlpatterns = [
    path("", views.index, name="index"),


    #ข่าว
    path('news', views.news, name="news"),
    path('news/<int:number>', views.news_content, name="news_content"),

    
    path('CompanyList', views.company, name="company"),
    path('Step1', Step1Form.as_view(), name="Step1"),
    path('Step2Admin',Step2Form.as_view(), name="Step2Admin"),
    path('Step2', views.step2U , name="Step2"),
    path('Step2/<str:pk>', views.step2A , name="Step2A"),
    path('Step1toPDF', views.Step1toPDF, name="Step1toPDF"),
    path('Step2toPDF', views.Step2toPDF, name="Step2toPDF"),
    path('Step3', views.step3, name="Step3"),
    path('Step4', views.step4, name="Step4"),
    path('Step5', views.step5, name="Step5"),
]
   