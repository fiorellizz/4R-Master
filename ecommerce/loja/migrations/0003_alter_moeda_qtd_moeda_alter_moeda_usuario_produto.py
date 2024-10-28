# Generated by Django 5.1.2 on 2024-10-21 19:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_moeda'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='moeda',
            name='qtd_moeda',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='moeda',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('qtd_disponivel', models.IntegerField(default=0)),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='loja.categoria')),
            ],
        ),
    ]
