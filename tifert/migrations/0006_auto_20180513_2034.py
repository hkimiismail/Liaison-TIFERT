# Generated by Django 2.0.5 on 2018-05-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tifert', '0005_auto_20180513_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to='Documents/images/%Y/%m/%d/'),
        ),
    ]
