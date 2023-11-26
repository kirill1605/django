from django.db import models

class Income(models.Model):
    operation_name = models.CharField(max_length=100, verbose_name='Название товара')
    payment_method = models.CharField(max_length=50, verbose_name='Способ оплаты')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    date = models.DateField(null=True, verbose_name='Дата')
    custom_field = models.CharField(max_length=100, default='', verbose_name='')

    def __str__(self):
        return self.operation_name

    class Meta:
        verbose_name = 'Доходы'
        verbose_name_plural = 'Доходы'