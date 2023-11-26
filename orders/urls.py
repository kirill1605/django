from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('', views.orders, name='orders'),
    path('create/', views.order_create, name='order_create'),
    path('edit/<int:order_id>/', views.order_update, name='order_update'),
    path('delete/<int:order_id>/', views.order_delete, name='order_delete'),
]
