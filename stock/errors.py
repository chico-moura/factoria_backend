from rest_framework import exceptions


class ProdutoNotFoundError(exceptions.APIException):
    status_code = 404
    default_code = 'produto_nao_encontrado'
    default_detail = 'Produto não encontrado'


class ContatoNotFoundError(exceptions.APIException):
    status_code = 404
    default_code = 'contato_nao_encontrado'
    default_detail = 'Contato não encontrado'
