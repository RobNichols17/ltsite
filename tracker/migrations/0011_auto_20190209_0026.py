# Generated by Django 2.1.5 on 2019-02-09 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20190208_1548'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadImages',
        ),
        migrations.AddField(
            model_name='catalog',
            name='catalog_img',
            field=models.ImageField(blank=True, null=True, upload_to='bottles/'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='imgname',
            field=models.CharField(blank=True, db_column='imgname', max_length=100, null=True),
        ),
    ]
