from enum import Enum
from pyUFbr.baseuf import ufbr


class ModelChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]


class IndicadorInscricaoEstaual(ModelChoiceEnum):
    CONTRIB = 'Contribuinte ICMS'
    ISENTO = 'Isento de cadastro'
    NAO_CONTRIB = 'Não contribuinte'


