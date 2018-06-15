import inspect
import random
import sys
from array import array
from timeit import timeit


def array_vs_list():
    int_list = [random.choice((0, 1)) for _ in range(100000)]
    bool_list = [random.choice((True, False)) for _ in range(100000)]
    byte_arr = array('b')
    byte_arr.extend(int_list)

    print(f'1:{sys.getsizeof(1)}')
    print(f'1000000000000000000:{sys.getsizeof(1000000000000000000)}')
    print(f'True:{sys.getsizeof(True)}')
    print(f'int_list:{sys.getsizeof(int_list)}')
    print(f'bool_list:{sys.getsizeof(bool_list)}')
    print(f'byte_arr:{sys.getsizeof(byte_arr)}')

    print('list access time: %f' % timeit('for r in randoms: int_list[r]',
                                          globals={'int_list': int_list, 'bool_list': bool_list, 'byte_arr': byte_arr},
                                          setup='import random; randoms = [random.randint(0, 99999) for _ in range(100)]'))

    print('array access time: %f' % timeit('for r in randoms: byte_arr[r]',
                                           globals={'int_list': int_list, 'bool_list': bool_list, 'byte_arr': byte_arr},
                                           setup='import random; randoms = [random.randint(0, 99999) for _ in range(100)]'))


def list_funcs():
    me = __import__(inspect.getmodulename(__file__))
    for name in dir(me):
        obj = getattr(me, name)
        if inspect.isfunction(obj):
            yield obj


if __name__ == '__main__':
    for func in list_funcs():
        print(f'running {func.__name__}...')
        func()
