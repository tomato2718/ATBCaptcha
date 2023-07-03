'''
Not for import.
'''

__all__ = ['arg_parser']

import argparse

from . import __about__

def arg_parser() -> argparse.ArgumentParser:
    '''
    Create argument parser for the project.
    
    :return: The parser created.
    :rtype: `argparse.ArgumentParser`
    '''
    parser = argparse.ArgumentParser(
        prog=__about__.__project__,
        description=__about__.__doc__,
        epilog=__about__.__usage__,
        add_help=False,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Program informations
    information = parser.add_argument_group('Program Informations')
    information.add_argument(
        '--help', '-h',
        action='help',
        help='Show this help message and exit.'
    )

    requirement = parser.add_argument_group('Requirement arguments')
    requirement.add_argument(
        'text',
        type=str,
        help='The text to display on captcha.',
    )
    requirement.add_argument(
        '--output', '-o',
        dest='output',
        action='store',
        type=str,
        help='The path of where the captcha to be save.',
        required=True
    )
    
    optional = parser.add_argument_group('Optional arguments')
    optional.add_argument(
        '--font',
        dest='font',
        action='store',
        type=str,
        help='Path of a TrueType font, HackNerdFont will be use as default if not specified.',
        default='',
    )

    optional.add_argument(
        '--size',
        dest='size',
        action='store',
        type=int,
        help='Size of the font, in pixels. (Default = 12)',
        default=12,
    )

    optional.add_argument(
        '--color',
        dest='color',
        choices=['default'],
        type=str,
        help='Color of the captcha, currently only dafault in supported.',
        default='default',
    )

    optional.add_argument(
        '--fps',
        dest='fps',
        choices=[15, 30],
        type=int,
        help='The fps of captcha. (Default = 15)',
        default=15,
    )
    
    return parser