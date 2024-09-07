
def print_sudoku(board: list[int]) -> None:
    for i in range(9):
        row = [str(board[i * 9 + j]) for j in range(9)]
        print(' '.join(row))


def clear_screen() -> None:
    print('\033[H\033[J')


def print_sudoku_and_solution(sudoku: list[int], solution: list[int]) -> None:
    clear_screen()

    for i in range(9):
        row = []
        for j in range(9):
            if sudoku[i * 9 + j] == 0:
                row.append(f'\033[1;31m{solution[i * 9 + j]}\033[0m')
            else:
                row.append(str(sudoku[i * 9 + j]))
        print(' '.join(row))
