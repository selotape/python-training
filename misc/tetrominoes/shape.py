from abc import ABC, abstractmethod
from typing import Iterable, Tuple


class Shape(ABC):
    rotation: int = None
    name: str = None

    @abstractmethod
    def moves(self) -> Iterable[Tuple[int, int]]:
        pass


class L(Shape):
    def __init__(self, clockwise_rotation):
        if clockwise_rotation % 90 != 0:
            raise ValueError('illegal shape rotation. Legal values are: [0, 90, 180, 270, ...]')
        self.rotation = clockwise_rotation
        self.name = 'L'

    def moves(self):
        yield (0, 0)
        if self.rotation % 360 == 0:
            yield (0, 1)
            yield (0, 1)
            yield (1, 0)
        elif self.rotation % 360 == 90:
            yield (1, 0)
            yield (1, 0)
            yield (-2, 1)
        elif self.rotation % 360 == 180:
            yield (0, 1)
            yield (0, 1)
            yield (-1, -2)
        elif self.rotation % 360 == 270:
            yield (0, -1)
            yield (-1, 1)
            yield (-1, 0)


L0 = L(0)
L90 = L(90)
L180 = L(180)
L270 = L(270)


class J(Shape):
    def __init__(self, clockwise_rotation):
        if clockwise_rotation % 90 != 0:
            raise ValueError('illegal shape rotation. Legal values are: [0, 90, 180, 270, ...]')
        self.rotation = clockwise_rotation
        self.name = 'J'

    def moves(self):
        yield (0, 0)
        if self.rotation % 360 == 0:
            yield (0, 1)
            yield (0, 1)
            yield (-1, 0)
        elif self.rotation % 360 == 90:
            yield (-1, 0)
            yield (-1, 0)
            yield (0, -1)
        elif self.rotation % 360 == 180:
            yield (0, -1)
            yield (0, -1)
            yield (1, 0)
        elif self.rotation % 360 == 270:
            yield (1, 0)
            yield (1, 0)
            yield (0, 1)


J0 = J(0)
J90 = J(90)
J180 = J(180)
J270 = J(270)
