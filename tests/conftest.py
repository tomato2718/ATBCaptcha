from os import path

import pytest

@pytest.fixture(scope='package')
def color() -> list[tuple[int, int, int]]:
    color = [
        (0, 0, 0),
        (50, 50, 50),
        (100, 100, 100),
        (150, 150, 150),
        (200, 200, 200),
        (252, 252, 252)
    ]
    return color

@pytest.fixture(scope='package')
def size() -> int:
    size = 12
    return size

@pytest.fixture(scope='package')
def font() -> str:
    font = path.join(
        path.dirname(__file__),
        '..',
        'atbcaptcha',
        'font',
        'Hack',
        'HackNerdFont-Regular.ttf'
    )
    return font

@pytest.fixture(scope='package')
def text() -> str:
    text = 'Testing'
    return text