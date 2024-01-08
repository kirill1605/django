from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'