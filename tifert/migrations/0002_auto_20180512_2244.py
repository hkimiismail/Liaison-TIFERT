# Generated by Django 2.0.5 on 2018-05-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tifert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaut_tabia',
            name='defaut',
            field=models.CharField(choices=[('Mécanique', 'Mécanique'), ('Q_Gypse', 'Qualité de Gypse'), ('Eléctrique', 'Eléctrique')], max_length=10),
        ),
    ]
