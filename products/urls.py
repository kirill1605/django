from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('add/', views.ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
]
