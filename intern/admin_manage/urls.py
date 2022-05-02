from django.urls import path


from . import views

app_name="admin_manage"

urlpatterns = [
    path("add_student", views.add_student, name="add_student"),
    path("add_student2", views.add_student2, name="add_student2"),
    path("admin_dashboard", views.admin_dashboard, name="admin_dashboard"),
    
    path('Step2', views.step2U , name="Step2"),
]
   