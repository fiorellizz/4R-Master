# Generated by Django 5.1.2 on 2024-10-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0009_alter_moeda_qtd_moeda'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='moeda',
            name='qtd_moeda',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
