from .meta_views import ManyInstancesAPI, SingleInstanceAPI

from stock.serializers import (
    ProdutoSerializer,
    ContatoSerializer)

from stock.repositories import (
    ProdutoRepo,
    ContatoRepo
)


class ProdutosAPI(ManyInstancesAPI):
    repo = ProdutoRepo
    serializer = ProdutoSerializer


class ProdutoDetailsAPI(SingleInstanceAPI):
    repo = ProdutoRepo
    serializer = ProdutoSerializer


class ContatoAPI(ManyInstancesAPI):
    repo = ContatoRepo
    serializer = ContatoSerializer


class ContatoDetailsAPI(SingleInstanceAPI):
    repo = ContatoRepo
    serializer = ContatoSerializer
