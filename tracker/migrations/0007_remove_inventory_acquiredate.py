# Generated by Django 2.1.5 on 2019-02-08 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20190204_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='acquiredate',
        ),
    ]