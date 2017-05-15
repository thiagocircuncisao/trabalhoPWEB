# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_auto_20170515_1605'),
        ('movimentacoes', '0002_auto_20170515_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoLancamentos',
            fields=[
                ('tipoLancamentosId', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='baixas',
            old_name='dataEmissao',
            new_name='dataBaixa',
        ),
        migrations.RemoveField(
            model_name='baixas',
            name='dataVencimento',
        ),
        migrations.RemoveField(
            model_name='baixas',
            name='empresaId',
        ),
        migrations.RemoveField(
            model_name='baixas',
            name='formasPagamentoId',
        ),
        migrations.RemoveField(
            model_name='baixas',
            name='tipoLancamento',
        ),
        migrations.RemoveField(
            model_name='baixas',
            name='valorTitulo',
        ),
        migrations.RemoveField(
            model_name='baixas',
            name='valorTitulo_currency',
        ),
        migrations.RemoveField(
            model_name='lancamentos',
            name='contaBancariaId',
        ),
        migrations.AddField(
            model_name='lancamentos',
            name='planoContasId',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='cadastros.PlanoContas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lancamentos',
            name='pendencia',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='lancamentos',
            name='tipoLancamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimentacoes.TipoLancamentos'),
        ),
    ]
