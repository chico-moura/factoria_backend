from django.contrib import admin
from stock.models import Contato, Produto, UnidadeDeMedida, Categoria

stock_models = [Contato, Produto, UnidadeDeMedida, Categoria]

admin.site.register(stock_models)
