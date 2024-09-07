
from typing import Callable


def solve_sudoku(
    sudoku: list[int],
    after_each_step_callback: Callable[[list[int]], None],
) -> list[int]:
    solution: list[int] = [0 for _ in range(81)]

    while True:
        solution.append(0)

        if after_each_step_callback:
            after_each_step_callback(solution)

    return solution
