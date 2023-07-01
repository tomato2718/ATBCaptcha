'''
Not for import.
'''

__all__ = ['random_pixels']
from random import sample

def random_pixels(style: list[tuple[int, int, int]],
                  length: int,
                  repeat: int) -> list[tuple[int, int, int]]:
    '''
    Return the list of random pixels according to the style input.

    .. note::
        This function will return the list of length = length * repeat

    For example::

        >>> color = [
                (0, 0, 0),
                (50, 50, 50),
                (100, 100, 100),
                (150, 150, 150),
                (200, 200, 200),
                (252, 252, 252)
            ]
        >>> random_pixels(
                style=color,
                length=2,
                repeat=3
            )

    Will return following result::

        [
            (100, 100, 100), (100, 100, 100), (100, 100, 100),
            (0, 0, 0), (0, 0, 0), (0, 0, 0),
        ]

    :param list[tuple[int, int, int]] style: The population to be sampled.
    :param int length: The length of the sample to be taken, `MUST` greater than 1.
    :param int repeat: The numbers of times that sample will be repeated.
    :return: List of the sample.
    :rtype: `list[tuple[int, int, int]]`
    :raise ValueError: When the input value of length <= 1.
    '''

    if length<=1:
        raise ValueError('The value of length MUST greater than 1.')
    if not isinstance(length, int):
        raise TypeError(f'length MUST be `int`, not {type(length)}.')
    
    while len(style) < length:
        style *= 2
    tmp = zip(
        *[
            sample(
                population=style,
                k=length
            )
        ]*repeat
    )
    res = []
    for frames in tmp:
        res += list(frames)
    return res