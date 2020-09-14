from stock.models import Produto, Contato
from abc import ABC
from rest_framework.exceptions import APIException
from stock.errors import ProdutoNotFoundError, ContatoNotFoundError


class Repository(ABC):
    model = Produto
    api_error404: APIException = None

    @classmethod
    def all(cls):
        return cls.model.objects.all()

    @classmethod
    def by_id(cls, id_):
        try:
            return cls.model.objects.get(id=id_)
        except cls.model.DoesNotExist:
            raise cls.api_error404


class ProdutoRepo(Repository):
    model = Produto
    api_error404 = ProdutoNotFoundError


class ContatoRepo(Repository):
    model = Contato
    api_error404 = ContatoNotFoundError

