import sys

import pytest


def subwords(x, length):
    mask = (1 << (length)) - 1
    while x:
        yield x & mask
        x >>= length


def parity(x):
    return sum(_parity_cache[subword] for subword in subwords(x, length=16)) % 2


def parities(numbers):
    return [parity(x) for x in numbers]


def _brute_parity(x: int):
    return count_bits(x) % 2


def count_bits(x):
    count = 0
    while x:
        count += 1
        x &= x - 1
    return count


_parity_cache = {n: _brute_parity(n) for n in range(1 << 16)}


def test_parity():
    assert parity(0) == 0
    assert parity(1) == 1
    assert parity(15) == 0


def test_subwords():
    assert list(subwords(7, 1)) == [1, 1, 1]
    assert list(subwords(1 << 4, 2)) == [0, 0, 1]


if __name__ == '__main__':
    pytest.main(sys.argv)
