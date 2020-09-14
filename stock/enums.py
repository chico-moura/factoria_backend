from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]


class IndicadorInscricaoEstaual(ChoiceEnum):
    CONTRIB = 'Contribuinte ICMS'
    ISENTO = 'Isento de cadastro'
    NAO_CONTRIB = 'Não contribuinte'
