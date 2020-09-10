from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from stock.enums import IndicadorInscricaoEstaual
from shared.address import estado_model_choices, cidade_model_choices


class Categoria(models.Model):
    nome = models.CharField(max_length=32)


class UnidadeDeMedida(models.Model):
    nome = models.CharField(max_length=4)


class Produto(models.Model):
    nome = models.CharField(max_length=64)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=True)
    unidade_medida = models.ForeignKey(UnidadeDeMedida, on_delete=models.PROTECT, null=True, blank=True)
    preco_compra = models.IntegerField(null=True, blank=True)
    preco_venda = models.IntegerField(null=True, blank=True)
    ean_gtin = models.IntegerField(null=True, blank=True)
    ncm = models.IntegerField(null=True, blank=True)
    produzido = models.BooleanField()
    observacoes = models.CharField(max_length=256)


class Contato(models.Model):
    nome = models.CharField(max_length=64)
    nome_fantasia = models.CharField(max_length=64, null=True, blank=True)
    cpf_cnpj = models.IntegerField(null=True, blank=True)
    indicador_ie = models.CharField(max_length=18, choices=IndicadorInscricaoEstaual.choices())
    ie = models.IntegerField(null=True, blank=True)
    nome_do_responsavel = models.CharField(max_length=32, null=True, blank=True)
    telefone = PhoneNumberField(blank=True)
    email = models.EmailField(null=True, blank=True)
    cep = models.IntegerField(null=True, blank=True)
    endereco = models.CharField(max_length=128, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=32, null=True, blank=True)
    bairro = models.CharField(max_length=32, null=True, blank=True)
    cidade = models.CharField(max_length=32, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    pais = models.CharField(max_length=32, null=True, blank=True)
    cliente = models.BooleanField(default=False)
    fornecedor = models.BooleanField(default=False)
    transportador = models.BooleanField(default=False)
