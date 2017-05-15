from django.contrib import admin
from .models import *
# Register your models here.


class UFAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']

class ContaBancariaAdmin(admin.ModelAdmin):
    list_display = ['numeroAgencia', 'numeroConta', 'descricao', 'saldo', 'banco']
    search_fields = ['numeroAgencia', 'numeroConta', 'descricao', 'saldo', 'banco']

class PlanoContasAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'classificacao']
    search_fields = ['descricao', 'classificacao']

class PessoaAdmin(admin.ModelAdmin):
    list_display = ['indentificacao', 'nome', 'email', 'telefone', 'cep']
    search_fields = ['indentificacao','nome', 'email', 'telefone', 'cep']

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nomeEmpresa', 'email', 'telefone', 'cep']
    search_fields = ['nomeEmpresa', 'email', 'telefone', 'cep']

class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']

admin.site.register(FormaPagamento, FormaPagamentoAdmin)
admin.site.register(Uf, UFAdmin)
admin.site.register(Muncipio, MunicipioAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(PlanoContas, PlanoContasAdmin)
admin.site.register(ContaBancaria, ContaBancariaAdmin)
