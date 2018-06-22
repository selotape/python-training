from collections.__init__ import namedtuple
from typing import Iterable, Tuple

from tetrominoes.shape import Shape

Cell = namedtuple("Cell", 'x,y')


class BoardException(Exception):
    pass


class IllegalBoardAction(BoardException):
    pass


class Board:
    def __init__(self, size):
        self._cells = [[0 for _ in range(size)] for _ in range(size)]
        self._size = size
        self._shapes_in_board = []

    def can_fit(self, shape: Shape, start_cell: Cell):
        return self.all_cells_available(start_cell, shape)

    def insert_shape(self, shape: Shape, start_cell: Cell):
        if not self.can_fit(shape, start_cell):
            raise IllegalBoardAction()
        self._fill_cells(start_cell, shape)
        self._shapes_in_board.append((shape.name, shape.rotation))
        return self

    def remove_shape(self, shape: Shape, start_cell: Cell):
        if not self._shapes_in_board:
            raise IllegalBoardAction()
        self._clear_cells(shape, start_cell)
        self._shapes_in_board.pop()
        return self

    def _clear_cells(self, shape: Shape, start_cell: Cell):
        for x, y in traverse(start_cell, shape.moves()):
            self._set_cell(x, y, 0)

    def all_cells_available(self, start_cell, shape):
        return all(self.is_cell_available(x, y) for x, y in traverse(start_cell, shape.moves()))

    def _fill_cells(self, start_cell, shape):
        for x, y in traverse(start_cell, shape.moves()):
            self._set_cell(x, y, 1)

    def _set_cell(self, x, y, v):
        self._cells[y][x] = v
        return self

    def __hash__(self):
        return hash(repr(self))

    @property
    def free_cells(self):
        return [Cell(x, y) for x in range(self._size) for y in range(self._size) if self.is_free(x, y)]

    @property
    def occupied_cells(self):
        return [Cell(x, y) for x in range(self._size) for y in range(self._size) if not self.is_free(x, y)]

    def is_free(self, x, y):
        return not bool(self._cells[y][x])

    def __repr__(self):
        rows = [''.join(str(d) for d in row) for row in self._cells]
        framed_rows = ['|' + r + '|\n' for r in rows]
        top_frame = ' ' + '_' * self._size + '\n'
        bottom_frame = ' ' + '‾' * self._size + '\n'
        return ''.join([top_frame] + framed_rows + [bottom_frame])

    def is_cell_available(self, x, y):
        size = self._size
        return 0 <= x < size and 0 <= y < size and self.is_free(x, y)


def empty_board(size):
    return Board(size)


def traverse(cell: Cell, moves: Iterable[Tuple[int, int]]):
    x, y = cell.x, cell.y
    for x_move, y_move in moves:
        x += x_move
        y += y_move
        yield x, y
