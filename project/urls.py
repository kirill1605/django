from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from products.views import ProductAPIView
from employees.views import EmployeeAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("home/", include("home.urls")),
    path("products/", include("products.urls")),
    path("employees/", include("employees.urls", namespace="employees")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("income/", include("income.urls", namespace="income")),
    path("expenses/", include("expenses.urls", namespace="expenses")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/productlist/", ProductAPIView.as_view(), name="product-list"),
    path("api/employeelist/", EmployeeAPIView.as_view(), name="employee-list"),
]
