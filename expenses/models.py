from django.db import models

class Expense(models.Model):
    operation_name = models.CharField(max_length=100, verbose_name='Название товара')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    custom_field = models.CharField(max_length=100, default='', verbose_name='')

    def __str__(self):
        return self.operation_name

    class Meta:
        verbose_name = 'Расходы'
        verbose_name_plural = 'Расходы'