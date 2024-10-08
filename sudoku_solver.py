
from operator import add
from typing import Callable

from sudoku_checker import check_board


def solve_sudoku(
    sudoku: list[int],
    after_each_step_callback: Callable[[list[int]], None],
) -> list[int]:
    solution: list[int] = [0 for _ in range(81)]

    def after_each_step_callback_safe(solution: list[int]):
        if after_each_step_callback:
            after_each_step_callback(solution)

    cursor: int = sudoku.index(0)

    while True:
        completed_board: list[int] = list(map(add, sudoku, solution))

        if check_board(completed_board):
            if 0 not in completed_board:
                print("Completed!")
                break

            cursor = completed_board.index(0)
            solution[cursor] += 1

            after_each_step_callback_safe(solution)
        else:
            if solution[cursor] < 9:
                solution[cursor] += 1
            else:
                while True:
                    solution[cursor] = 0
                    after_each_step_callback_safe(solution)

                    while solution[cursor] == 0:
                        cursor -= 1

                    if solution[cursor] < 9:
                        solution[cursor] += 1

                        after_each_step_callback_safe(solution)
                        break

    return solution
