import moneyed
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone
from cadastros.models import *
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save



class TipoLancamentos(models.Model):
    tipoLancamentosId = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name="Tipo de Lancamento"
        verbose_name_plural="Tipos de Lancamentos"


# Create your models here.
class Lancamentos(models.Model):
    lancamentosId = models.AutoField(primary_key=True)
    pessoaId = models.ForeignKey(Pessoa)
    empresaId = models.ForeignKey(Empresa)
    planoContasId = models.ForeignKey(PlanoContas)
    tipoLancamento = models.ForeignKey(TipoLancamentos)
    numeroDocumento = models.CharField(max_length=20)
    dataVencimento = models.DateField()
    dataEmissao = models.DateField()
    pendencia = models.BooleanField(default=True)
    valorTitulo = MoneyField(max_digits=100, decimal_places=2, default_currency="BRL")
    empresaId = models.ForeignKey(Empresa)

    def __str__(self):
        return str(self.numeroDocumento + ' ' + self.planoContasId.descricao)

    class Meta:
        verbose_name="Lancamento"
        verbose_name_plural="Lancamentos"

class Baixas(models.Model):
    baixasId = models.AutoField(primary_key=True)
    lancamentosId = models.ForeignKey(Lancamentos)
    numeroDocumento = models.CharField(max_length=20)
    dataBaixa = models.DateField()

    def __str__(self):
        return str(self.baixasId)

    class Meta:
        verbose_name="Baixa"
        verbose_name_plural="Baixas"


class Tesouraria(models.Model):
    tesourariaId = models.AutoField(primary_key=True)
    formasPagamentoId = models.ForeignKey(FormaPagamento)
    empresaId = models.ForeignKey(Empresa)
    pessoaId = models.ForeignKey(Pessoa)
    planoContasId = models.ForeignKey(PlanoContas)

    def __str__(self):
        return str(self.tesourariaId)

    class Meta:
        verbose_name="Tesouraria"
        verbose_name_plural="Tesouraria"

@receiver(post_save, sender=Baixas)
def alterar_saldo_conta_signal(sender, instance, **kwargs):
    print(str(instance.lancamentosId.planoContasId.contaBancariaId.saldo))
    print(str(instance.lancamentosId.tipoLancamento.tipoLancamentosId))
    if(instance.lancamentosId.tipoLancamento.tipoLancamentosId == 1):
        print(str(instance.lancamentosId.valorTitulo))
        instance.lancamentosId.planoContasId.contaBancariaId.saldo = instance.lancamentosId.planoContasId.contaBancariaId.saldo + instance.lancamentosId.valorTitulo
    elif(instance.lancamentosId.tipoLancamento.tipoLancamentosId == 2):
        print(str(instance.lancamentosId.valorTitulo))
        instance.lancamentosId.planoContasId.contaBancariaId.saldo = instance.lancamentosId.planoContasId.contaBancariaId.saldo - instance.lancamentosId.valorTitulo
    instance.lancamentosId.pendencia = False
    instance.lancamentosId.save()
    instance.lancamentosId.planoContasId.contaBancariaId.save()
