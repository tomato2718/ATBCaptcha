import pytest

from atbcaptcha._utils import random_pixels

##### FIXTURES #####


##### TESTS #####
def test_random_pixels(color):
    with pytest.raises(ValueError):
        test = random_pixels(
            style=color,
            length=1,
            repeat=1
        )

    for rep in range(1, 10):
        test = random_pixels(
            style=color,
            length=3,
            repeat=rep
        )
        for i in range(0, len(test), rep):
            assert len(set(test[i:i+rep])) == 1
