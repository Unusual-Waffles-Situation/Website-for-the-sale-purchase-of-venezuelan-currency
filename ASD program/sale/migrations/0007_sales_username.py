# Generated by Django 4.0.3 on 2022-03-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0006_alter_sales_price_alter_sales_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]