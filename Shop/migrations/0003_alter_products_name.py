# Generated by Django 5.0 on 2023-12-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_category_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Назва'),
        ),
    ]
