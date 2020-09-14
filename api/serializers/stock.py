from rest_framework import serializers
from stock.models import Produto, DefaultModel, Contato


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        exclude = []


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        exclude = []
