from datetime import datetime
from typing import Dict, Iterable, Set

from tetrominoes.board import Board, empty_board
from tetrominoes.shape import Shape, L0, L90, L180, L270, J0, J90, J180, J270

BOARD_SIZE = 6


def legal_boards(board: Board, legal_shapes: Iterable[Shape],
                 required_shapes: int, cache: Dict[Board, Set[str]]) -> Set[str]:
    if board in cache:
        return cache[board]

    all_legal_boards = set()
    if required_shapes <= 0:
        all_legal_boards.add(repr(board))
    else:
        for free_cell in board.free_cells:
            for l in legal_shapes:
                if board.can_fit(l, free_cell):
                    board.insert_shape(l, free_cell)
                    all_legal_boards |= legal_boards(board, legal_shapes, required_shapes - 1, cache)
                    board.remove_shape(l, free_cell)
    cache[board] = all_legal_boards
    return all_legal_boards


def solve_tetrominoes_riddle():
    print('%s: Calculating Legal L_Boards...' % str(datetime.now()))
    legal_L_boards = legal_boards(empty_board(BOARD_SIZE), (L0, L90, L180, L270), 5, {})
    print('%s: Calculating Legal J_Boards...' % str(datetime.now()))
    legal_J_boards = legal_boards(empty_board(BOARD_SIZE), (J0, J90, J180, J270), 5, {})
    for b in legal_L_boards & legal_J_boards:
        print(b)


if __name__ == '__main__':
    solve_tetrominoes_riddle()
