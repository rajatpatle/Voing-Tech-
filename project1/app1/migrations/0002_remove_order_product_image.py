# Generated by Django 4.1.4 on 2022-12-11 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_image',
        ),
    ]
