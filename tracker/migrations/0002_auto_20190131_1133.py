# Generated by Django 2.1.5 on 2019-01-31 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.IntegerField(blank=True, db_column='quantity', null=True),
        ),
    ]
