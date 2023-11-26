from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.employee_list, name='employees'),
    path('add/', views.add_employee, name='add'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete'),
]