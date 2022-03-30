from django.urls import path

from . import views

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
    path('test', views.test, name="test"),
]
   