
from time import sleep
from sudoku_io import read_board, write_board
from sudoku_printer import print_sudoku_and_solution
from sudoku_solver import solve_sudoku


def after_each_step_callback(solution: list[int]) -> None:
    print_sudoku_and_solution(sudoku, solution)
    sleep(0.0001)


sudoku: list[int] = read_board("sample_data/sample_input.txt")

solution: list[int] = solve_sudoku(
    sudoku,
    after_each_step_callback=after_each_step_callback,
)

write_board("sample_data/sample_output.txt", solution)
