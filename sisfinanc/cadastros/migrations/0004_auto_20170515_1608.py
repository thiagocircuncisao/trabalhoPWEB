# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 19:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_auto_20170515_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planocontas',
            name='banco',
        ),
        migrations.RemoveField(
            model_name='planocontas',
            name='caixa',
        ),
        migrations.RemoveField(
            model_name='planocontas',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='planocontas',
            name='entradaRecurso',
        ),
        migrations.RemoveField(
            model_name='planocontas',
            name='fornecedor',
        ),
        migrations.RemoveField(
            model_name='planocontas',
            name='saidaRecurso',
        ),
        migrations.RemoveField(
            model_name='planocontas',
            name='tipoConta',
        ),
    ]
