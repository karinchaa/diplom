# Generated by Django 5.0 on 2023-12-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_category_img_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img_cat',
            field=models.ImageField(default='img_category/category.jpg', upload_to='img_category'),
        ),
    ]
