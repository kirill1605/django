# Generated by Django 4.2.2 on 2023-06-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_remove_product_expenses_remove_product_incomes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='custom_field',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]
