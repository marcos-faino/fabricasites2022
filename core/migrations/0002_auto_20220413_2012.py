# Generated by Django 3.2.12 on 2022-04-14 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionario',
            options={'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários'},
        ),
        migrations.AlterModelOptions(
            name='servico',
            options={'verbose_name': 'Serviço', 'verbose_name_plural': 'Serviços'},
        ),
    ]
