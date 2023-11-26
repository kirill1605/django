from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.expenses_list, name='expenses'),
    path('add/', views.expense_add, name='expense_add'),
    path('edit/<int:expense_id>/', views.expense_edit, name='expense_edit'),
    path('delete/<int:expense_id>/', views.expense_delete, name='expense_delete'),
]
