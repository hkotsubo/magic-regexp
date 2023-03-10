import re
from enum import Enum
from typing import Any, Callable, Union


def debug(msg: Any):
    print(f'RegexBuilder::debug --> {msg}')


class Tipos:
    qualquer = '.'
    numero = '\d'
    fora_numero = '\D'
    letra = '\w'
    fora_letra = '\W'
    espaco_em_branco = '\s'
    fora_espaco_em_branco = '\S'

    def intervalo(self, inicio: Any, fim: Any):
        return f'[{inicio}-{fim}]'


class Flags(Enum):
    ASCII = re.ASCII
    IGNORECASE = re.IGNORECASE
    MULTILINE = re.MULTILINE
    DOTALL = re.DOTALL


def flags_parser(data: Any):
    flags = 0
    for flag in data:
        flags |= flag.value

    return flags


class RegexConstrutor:
    def __init__(self):
        self._regex_string = str()
        self._regex_object = None

        self.tipos = Tipos()

    def contenha(self, texto: str):
        self._regex_string += texto
        return self

    def comeca_com(self, texto: str):
        self._regex_string += '^' + texto
        return self

    def termina_com(self, texto: str):
        self._regex_string += texto + '$'
        return self

    def zero_ou_um(self, texto: str):
        self._regex_string += texto + '?'
        return self

    def zero_ou_mais(self, texto: str):
        self._regex_string += texto + '*'
        return self

    def um_ou_mais(self, texto: str):
        self._regex_string += texto + '+'
        return self

    def exatamente_n(self, vezes: int, texto: str):
        self._regex_string += texto + '{' + str(vezes) + '}'
        return self

    def n_ou_mais(self, vezes: int, texto: str):
        self._regex_string += texto + '{' + str(vezes) + ',}'
        return self

    def construir(self, *flags: Flags):
        self._regex_object = re.compile(
            r'' + self._regex_string,
            flags_parser(flags),
        )

        self._regex_string = str()

        debug(self._regex_object)

        return self._regex_object
