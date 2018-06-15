import sys

import pytest


def parities(numbers):
    return [parity(x) for x in numbers]


def parity(x: int):
    return count_bits(x) % 2


def count_bits(x):
    count = 0
    while x:
        count += 1
        x = x & (x - 1)
    return count


def test_parity():
    assert parity(0) == 0
    assert parity(1) == 1
    assert parity(15) == 0


if __name__ == '__main__':
    pytest.main(sys.argv)
