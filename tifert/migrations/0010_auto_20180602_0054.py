# Generated by Django 2.0.5 on 2018-06-01 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tifert', '0009_auto_20180602_0046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image',
            new_name='file',
        ),
    ]