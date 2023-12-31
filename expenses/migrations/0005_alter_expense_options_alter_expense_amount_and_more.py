# Generated by Django 4.2.2 on 2023-07-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_expense_custom_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name': 'Расходы', 'verbose_name_plural': 'Расходы'},
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='custom_field',
            field=models.CharField(default='', max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='operation_name',
            field=models.CharField(max_length=100, verbose_name='Название товара'),
        ),
    ]
