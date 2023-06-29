from random import randint

# TODO: random color class

def random_color() -> tuple[int, int, int]:
    return tuple(randint(0, 225) for i in range(3))
