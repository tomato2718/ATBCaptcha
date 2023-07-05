'''
Not for import.
'''

__all__ = [
    'Font',
    'Color',
]

from os import path
from typing import Any

class FontMeta(type):
    '''
    Meta class make Font class return absolute path instead of relative path.
    '''
    def __getattribute__(self, __name: str) -> Any:
        res = object.__getattribute__(self, __name)
        if isinstance(res, str):
            res = path.join(path.dirname(__file__), 'font', res)
        return res
    
class Font(metaclass=FontMeta):
    '''
    Class for storing the paths of currently supported fonts.
    '''
    HACK_NERD_FONT = 'Hack/HackNerdFont-Regular.ttf'

# TODO: add more colors

class Color:
    '''
    Recommanded color to use.
    '''
    DEFAULT = [
        (0, 0, 0),
        (50, 50, 50),
        (100, 100, 100),
        (150, 150, 150),
        (200, 200, 200),
        (252, 252, 252),
    ]