from django.urls import path

from . import views

app_name="main"

urlpatterns = [
    path("", views.index, name="index"),
    path("start/", views.start, name="start"),
    
    #ข่าว
    path('news', views.news, name="news"),
    path('news/<pk>', views.news_content, name="news_content"),
]
   