from django.contrib import admin
from movimentacoes.models import *
# Register your models here.
REPORT_BUILDER_INCLUDE = ['Baixas', 'Lancamentos', 'Tesouraria']
REPORT_BUILDER_GLOBAL_EXPORT = True
REPORT_BUILDER_FRONTEND = False
