from time import sleep


class Board:
    """Put your solution here"""

    def __init__(self, width: int = 3, height: int = 3):
        self.height = height
        self.width = width
        self.board = []
        for _ in range(self.height):
            row = [False] * self.width
            self.board.append(row)

    def __str__(self):
        """Return a string representation of a board.

        Use small o for alive cells and period for empty cells.
        E.g. for board 3x3 with simplest oscillator:
        .o.
        .o.
        .o.
        """
        alive_cell = "o"  # noqa
        empty = "."  # noqa
        new_line = "\n"  # noqa
        return str(self.board)

    def place_cell(self, row: int, col: int):
        """Make a cell alive."""
        pass

    def toggle_cell(self, row: int, col: int) -> None:
        """Invert state of the cell."""
        pass

    def is_alive(self, row: int, col: int) -> bool:
        pass

    def next(self) -> None:
        pass


if __name__ == "__main__":
    board = Board(3, 3)
    for i in range(3):
        board.place_cell(1, i)

    for i in range(100):
        print(board)
        board.next()
        sleep(0.5)
