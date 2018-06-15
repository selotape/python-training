def print_bin_float(f):
    if f > 1.0 or f < 0:
        return 'ERROR'

    bin_rep = ['0.']
    while f > 0.0:
        if len(bin_rep) > 32:
            return 'ERROR'

        f *= 2
        if f >= 1.0:
            bin_rep.append('1')
            f -= 1
        else:
            bin_rep.append('0')

    return ''.join(bin_rep)


def test_bin_float():
    assert 'ERROR' == print_bin_float(1.5)
    assert '0.1' == print_bin_float(0.5)
    assert '0.11' == print_bin_float(0.75)
    assert '0.101' == print_bin_float(1 / 2 + 1 / (2 ** 3))


def bits(num):
    while num > 0:
        yield num & 1
        num >>= 1


def flip_bit_to_win(num):
    if num == -1:
        return 32

    prev_strech = 0
    cur_strech = 0
    best_seen = 0
    for bit in bits(num):
        if bit:
            cur_strech += 1
        else:
            best_seen = max(best_seen, (cur_strech + prev_strech + 1))
            cur_strech, prev_strech = 0, cur_strech

    best_seen = max(best_seen, (cur_strech + prev_strech + 1))

    return best_seen


def test_flip_bit_to_win():
    assert 2 == flip_bit_to_win(1)
    assert 3 == flip_bit_to_win(3)
    assert 2 == flip_bit_to_win(2)

    assert '11011101110' == '{0:b}'.format((7 | 7 << 4 | 3 << 8) << 1)
    assert 7 == flip_bit_to_win((7 | 7 << 4 | 3 << 8) << 1)
