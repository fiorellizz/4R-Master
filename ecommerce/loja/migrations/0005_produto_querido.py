# Generated by Django 5.1.2 on 2024-10-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_produto_preco_alter_moeda_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='querido',
            field=models.BooleanField(default=False),
        ),
    ]
