from django.db import models
from employees.models import Employee

class Order(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    delivery_address = models.CharField(max_length=200, verbose_name='Адрес доставки')
    employees = models.ManyToManyField(Employee, verbose_name='Сотрудник')
    date = models.DateField(null=True, verbose_name='Дата')
    def __str__(self):
        return self.product_name

class OrderEmployee(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Название заказа')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    date = models.DateField(null=True)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.order.product_name}"

    class Meta:
        db_table = 'orders_order_employee'