# Generated by Django 4.0.3 on 2022-03-13 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0007_sales_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='type',
            field=models.CharField(choices=[('Compra', 'Compra'), ('Venta', 'Venta')], default='Venta', max_length=6),
        ),
    ]
