
def check_board(board: list[int]) -> bool:
    return check_rows(board) and check_columns(board) and check_squares(board)


def check_rows(board: list[int]) -> bool:
    for i in range(9):
        row = [board[i * 9 + j] for j in range(9)]
        if not check_numbers(row):
            return False
    return True


def check_columns(board: list[int]) -> bool:
    for i in range(9):
        column = [board[j * 9 + i] for j in range(9)]
        if not check_numbers(column):
            return False
    return True


def check_squares(board: list[int]) -> bool:
    for i in range(3):
        for j in range(3):
            square = [board[(i * 3 + k) * 9 + j * 3 + l]
                      for k in range(3) for l in range(3)]
            if not check_numbers(square):
                return False
    return True


def check_numbers(numbers: list[int]) -> bool:
    numbers = [number for number in numbers if number != 0]
    return len(numbers) == len(set(numbers))
