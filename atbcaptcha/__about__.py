'''
Informations about the project.
'''

__all__ = [
    '__project__',
    '__version__',
    '__author__',
    '__maintainer__',
    '__release__',
    '__summary__',
    '__usage__'
]

__project__ = 'ATBCaptcha'
__version__ = '0.3.0-dev'
__author__ = 'yveschen2718@gmail.com'
__maintainer__ = 'yveschen2718@gmail.com'
__release__ = '2023/07/03'
__summary__ = 'Animated Text-Based Captcha'
__usage__ = f'''
Usage:
    >>> python -m atbcaptcha -h
    >>> python -m atbcaptcha foo -o ./output.gif
    >>> python -m atbcaptcha bar -o ./output.gif --size 72
    >>> python -m atbcaptcha foobar -o ./output.gif --size 72 --fps 30   
'''