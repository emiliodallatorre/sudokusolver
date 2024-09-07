
def read_board(file_path: str) -> list[int]:
    with open(file_path, 'r') as file:
        return [int(cell) for cell in file.read() if cell.isdigit()]


def write_board(file_path: str, board: list[int]) -> None:
    with open(file_path, 'w') as file:
        for cell in board:
            file.write(str(cell))
