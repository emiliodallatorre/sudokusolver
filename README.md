# Sudoku Solver using DFS in Python

This is a Python implementation of a Sudoku solver that uses Depth First Search (DFS) to explore potential solutions and resolve a given Sudoku puzzle.

## Features
- Solves a standard 9x9 Sudoku puzzle
- Uses DFS and backtracking to explore valid solutions
- Handles puzzles with unique solutions

## Prerequisites
- Python 3.x

## How it works
The algorithm follows these steps:
1. Find an empty cell in the Sudoku grid
2. Attempt to place numbers 1 through 9 in the empty cell, ensuring that no number violates Sudoku rules
3. If a number fits, recursively proceed to the next empty cell
4. If no number fits, backtrack to the previous cell and try the next valid number
5. Repeat until the puzzle is solved or determined unsolvable

## Usage

To resolve a Sudoku puzzle, you can use the `solve_sudoku` function from the `sudoku_solver` module. The function takes a Sudoku board as input and returns the solved board as output.

```python
from time import sleep
from sudoku_io import read_board, write_board
from sudoku_printer import print_sudoku_and_solution
from sudoku_solver import solve_sudoku


def after_each_step_callback(solution: list[int]) -> None:
    print_sudoku_and_solution(sudoku, solution)
    sleep(0.005)


sudoku: list[int] = read_board("sample_data/sample_input.txt")
solution: list[int] = solve_sudoku(
    sudoku,
    after_each_step_callback=after_each_step_callback,
)

write_board("sample_data/sample_output.txt", solution)
```

You can specify a callback function to be called after each step of the solving process. This can be useful for visualizing the solving process or tracking the algorithm's progress.
This project comes with a simple printer that displays the Sudoku board and the current solution in the console.
