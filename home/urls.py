from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('products/', include('products.urls', namespace='products')),
    path('employees/', include('employees.urls', namespace='employees')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('income/', include('income.urls', namespace='income')),
    path('expenses/', include('expenses.urls', namespace='expenses')),
]