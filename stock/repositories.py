from stock.models import Produto, Contato
from abc import ABC


class Repository(ABC):
    model = Produto

    @classmethod
    def all(cls):
        return cls.model.objects.all()

    @classmethod
    def by_id(cls, id_):
        return cls.model.objects.all(id=id_)


class ProdutoRepo(Repository):
    model = Produto


class ContatoRepo(Repository):
    model = Contato
