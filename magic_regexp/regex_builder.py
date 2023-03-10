import re
from enum import Enum
from typing import Any, Union


def debug(msg: Any):
    print(f'RegexBuilder::debug --> {msg}')


class Types(Enum):
    any = '.'


def types_parser(data: Union[str, Types]):
    if not isinstance(data, Types):
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


class RegexBuilder:
    def __init__(self):
        self._regex_string = str()
        self._builded = False
        self._regex_object = None

    def contain(self, string: Union[str, Types]):
        self._regex_string += types_parser(string)
        return self

    def begins_with(self, string: Union[str, Types]):
        self._regex_string += '^' + types_parser(string)
        return self

    def ends_with(self, string: Union[str, Types]):
        self._regex_string += types_parser(string) + '$'
        return self

    def build(self, *flags: Flags):
        self._regex_object = re.compile(
            r'' + self._regex_string, flags_parser(flags)
        )
        self._builded = True
        debug(self._regex_object)
        return self._regex_object
