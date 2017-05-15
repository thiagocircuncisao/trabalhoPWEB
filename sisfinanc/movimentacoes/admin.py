from django.contrib import admin
from .models import *

class LancamentosAdmin(admin.ModelAdmin):
    list_display = ['numeroDocumento', 'tipoLancamento', 'valorTitulo', 'dataEmissao', 'dataVencimento']
    search_fields = ['numeroDocumento', 'tipoLancamento', 'valorTitulo', 'dataEmissao', 'dataVencimento']

class BaixasAdmin(admin.ModelAdmin):
    list_display = ['numeroDocumento']
    search_fields = ['numeroDocumento']

class TesourariaAdmin(admin.ModelAdmin):
    list_display = ['tesourariaId', 'formasPagamentoId', 'empresaId', 'pessoaId', 'planoContasId']
    search_fields = ['tesourariaId', 'formasPagamentoId', 'empresaId', 'pessoaId', 'planoContasId']

class TipoLancamentosAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']

# Register your models here.
admin.site.register(Lancamentos, LancamentosAdmin)
admin.site.register(Baixas, BaixasAdmin)
admin.site.register(Tesouraria, TesourariaAdmin)
admin.site.register(TipoLancamentos, TipoLancamentosAdmin)
