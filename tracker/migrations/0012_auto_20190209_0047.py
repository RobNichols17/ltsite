# Generated by Django 2.1.5 on 2019-02-09 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_auto_20190209_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='catalog_img',
            field=models.ImageField(blank=True, null=True, upload_to='bottles'),
        ),
    ]
