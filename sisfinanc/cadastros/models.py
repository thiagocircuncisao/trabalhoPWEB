import moneyed
from djmoney.models.fields import MoneyField
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

# Create your models here.


class Uf(models.Model):
    ufId = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50,verbose_name="Estado")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name="Estado"
        verbose_name_plural="Estados"

class Muncipio(models.Model):
    municipioId = models.AutoField(primary_key=True)
    ufId = models.ForeignKey(Uf)
    descricao = models.CharField(max_length=255, verbose_name="Município")

    class Meta:
        verbose_name="Municipio"
        verbose_name_plural="Municipios"

    def __str__(self):
        return self.descricao

class ContaBancaria(models.Model):
    contaBancariaId = models.AutoField(primary_key=True)
    classificacao = models.CharField(max_length=18, verbose_name="Classificação")
    descricao = models.CharField(max_length=50)
    numeroAgencia = models.CharField(max_length=20, verbose_name="Agência")
    numeroConta = models.CharField(max_length=20, verbose_name="Conta")
    dataSaldoInicial = models.DateField()
    saldo = MoneyField(max_digits=100, decimal_places=2, default_currency="BRL")
    banco = models.CharField(max_length=3)

    class Meta:
        verbose_name="Conta Bancária"
        verbose_name_plural="Contas Bancarias"

    def __str__(self):
        return str(self.numeroAgencia + ' ' + self.numeroConta)

class PlanoContas(models.Model):
    planoContasId = models.AutoField(primary_key=True)
    contaBancariaId = models.ForeignKey(ContaBancaria)
    classificacao = models.CharField(max_length=18)
    descricao = models.CharField(max_length=50)

    class Meta:
        verbose_name="Plano de Contas"
        verbose_name_plural="Planos de Contas"

    def __str__(self):
        return self.descricao

class Pessoa(models.Model):
    pessoaId =  models.AutoField(primary_key=True)
    CPFouCNPJ = models.CharField(max_length=15)
    indentificacao = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=50)
    ufId = models.ForeignKey(Uf)
    municipioID = models.ForeignKey(Muncipio)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.CPFouCNPJ

    class Meta:
        verbose_name="Pessoa"
        verbose_name_plural="Pessoas"

class Empresa(models.Model):
    empresaId = models.AutoField(primary_key=True)
    titularId = models.ForeignKey(Pessoa)
    nomeEmpresa = models.CharField(max_length=50)
    razaoSocial = models.CharField(max_length=255)
    inscricaoEstadual =  models.CharField(max_length=20)
    inscricaoMunicipal = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=50)
    ufId = models.ForeignKey(Uf, 'ufId', verbose_name='Estado')
    municipioID = models.ForeignKey(Muncipio, 'municipioId', verbose_name='Município')
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.nomeEmpresa

    class Meta:
        verbose_name="Empresa"
        verbose_name_plural="Empresas"

class FormaPagamento(models.Model):
    formaPagamentoId = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name="Forma de Pagamento"
        verbose_name_plural="Formas de Pagamento"
