# Generated by Django 4.2.2 on 2023-06-29 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_expense_income_product_expenses_product_incomes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='expenses',
        ),
        migrations.RemoveField(
            model_name='product',
            name='incomes',
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.DeleteModel(
            name='Income',
        ),
    ]
