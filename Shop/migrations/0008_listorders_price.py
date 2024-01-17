# Generated by Django 5.0 on 2023-12-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_listorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='listorders',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Ціна замовлення'),
        ),
    ]
