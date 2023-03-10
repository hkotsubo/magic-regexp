import re
from enum import Enum
from typing import Any, Union


def debug(msg: Any):
    print(f'RegexBuilder::debug --> {msg}')


class Tipos(Enum):
    caracter = '.'
    numero = '\d'


def tipos_parser(data: Union[str, Tipos]):
    if not isinstance(data, Tipos):
        return str(data)
    return str(data.value)


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
        self._regex_texto = str()
        self._builded = False
        self._regex_object = None

    def contenha(self, texto: Union[str, Tipos]):
        self._regex_texto += tipos_parser(texto)
        return self

    def comeca_com(self, texto: Union[str, Tipos]):
        self._regex_texto += '^' + tipos_parser(texto)
        return self

    def termina_com(self, texto: Union[str, Tipos]):
        self._regex_texto += tipos_parser(texto) + '$'
        return self

    def zero_ou_um(self, texto: Union[str, Tipos]):
        self._regex_texto += tipos_parser(texto) + '?'
        return self

    def zero_ou_mais(self, texto: Union[str, Tipos]):
        self._regex_texto += tipos_parser(texto) + '*'
        return self

    def um_ou_mais(self, texto: Union[str, Tipos]):
        self._regex_texto += tipos_parser(texto) + '+'
        return self

    def exatamente_n(self, vezes: int, texto: Union[str, Tipos]):
        self._regex_texto += tipos_parser(texto) + '{' + str(vezes) + '}'
        return self

    def n_ou_mais(self, vezes: int, texto: Union[str, Tipos]):
        self._regex_texto += tipos_parser(texto) + '{' + str(vezes) + ',}'
        return self

    def construir(self, *flags: Flags):
        self._regex_object = re.compile(
            r'' + self._regex_texto, flags_parser(flags)
        )
        self._builded = True
        debug(self._regex_object)
        return self._regex_object
