__all__ = ['Font']

from os import path
from typing import Any

class FontMeta(type):
    '''
    Meta class make Font class return absolute path instead of relative path.
    '''
    def __getattribute__(self, __name: str) -> Any:
        res = object.__getattribute__(self, __name)
        if isinstance(res, str):
            res = path.join(path.dirname(__file__), 'etc', res)
            print(res)
        return res
    
class Font(metaclass=FontMeta):
    '''
    Class for storing the paths of currently supported fonts.
    '''
    HACK_NERD_FONT = 'Hack/HackNerdFont-Regular.ttf'