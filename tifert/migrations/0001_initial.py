# Generated by Django 2.0.5 on 2018-05-11 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Defaut_tabia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defaut', models.CharField(choices=[('M', 'Mécanique'), ('Q', 'Qualité de Gypse'), ('E', 'Eléctrique')], max_length=1)),
                ('h_a_tabia', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Arrêt tabia(Heure,min)')),
                ('message', models.TextField()),
                ('doc', models.FileField(upload_to='tabia/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Defaut_tabia',
                'ordering': ['-jour'],
            },
        ),
        migrations.CreateModel(
            name='Rj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='DATE')),
                ('h_m_h2so4', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='heure de marche sulfurique')),
                ('fqh_p_h2so4', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='FQ (j-1) production')),
                ('fqa_p_h2so4', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='FQ (j) production')),
                ('p_acide_h2so4', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Production H2SO4')),
                ('sh_acide_h2so4', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Stock H2SO4 (j-1)')),
                ('tk2_1', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='7560 TK2/1 (T)')),
                ('tk2_2', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='7560 TK2/2 (T)')),
                ('titre_p_h2so4', models.DecimalField(decimal_places=4, max_digits=4, verbose_name='Titre H2SO4 produit')),
                ('sh_s', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Stock Soufre (j-1)')),
                ('sa_s', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Stock Soufre (j)')),
                ('s_c', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Soufre consommé')),
                ('p_s_liq', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Prod soufre liquide')),
                ('r_s_solid', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Reception soufre solide')),
                ('tk1_1', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='7530 TK1/1 (T)')),
                ('tk1_2', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='7530 TK1/2 (T)')),
                ('fqd_t_h2so4', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='FQ tr(début)')),
                ('fqf_t_h2so4', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='FQ tr(fin)')),
                ('t_acide_h2so4', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='transfert H2SO4')),
                ('titre_t_h2so4', models.DecimalField(decimal_places=4, max_digits=4, verbose_name='Titre H2SO4 produit')),
                ('p_acide_h3po4', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Production H3PO4 (T)')),
                ('h_a_gypse', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Arrêt tabia (heure,minute)')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Rj',
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='defaut_tabia',
            name='jour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jours', to='tifert.Rj'),
        ),
    ]
