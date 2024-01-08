from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User

class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    position = models.CharField(max_length=100, verbose_name='Должность')
    age = models.IntegerField(verbose_name='Возраст')
    salary = models.IntegerField(verbose_name='Зарплата')
    date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    history = HistoricalRecords()

    orders = models.ManyToManyField('orders.Order', through='orders.OrderEmployee')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
