# Generated by Django 4.2.2 on 2023-06-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_custom_field_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderemployee',
            name='date',
            field=models.DateField(null=True),
        ),
    ]