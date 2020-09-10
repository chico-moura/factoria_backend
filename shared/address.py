from pyUFbr.baseuf import ufbr


def tuplify(list_: []) -> [()]:
    return [(item, item) for item in list_]


def estado_model_choices() ->[()]:
    return tuplify(ufbr.list_uf)


def cidade_model_choices(estado: str) -> [()]:
    return tuplify(ufbr.list_cidades(estado))
