from time import sleep


class Board:
    """Put your solution here"""

    def __init__(self, width: int = 3, height: int = 3):
        self.height = height
        self.width = width
        self.board = []
        self.next_board = [[False, False, False], [False, False, False], [False, False, False]]
        # self.next_board  - вспомогательная доска, нужна для того, чтобы не изменять self.board при выполнении метода toggle
        # почему-то, когда я добавляю self.next_board в цикл ниже, чтобы так же заполнить её False,
        # происходит необъяснимый баг, поэтому пока так

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
        result = ''
        for row_i, row in enumerate(self.board):
            result += new_line
            row_str = [alive_cell if self.is_alive(row_i, col_i) else empty for col_i in range(len(row))]
            result += ''.join(row_str)
        return result

    def place_cell(self, row: int, col: int) -> None:
        if not self.board[row][col]:
            self.board[row][col] = True

    def toggle_cell(self, row: int, col: int) -> None:
        """Invert state of the cell."""
        cell_neigbours_pos = []  # создаю пустой список с позициями всех соседей клетки
        # определяю границы, чтобы не выйти за границы board
        up_border = -1
        down_border = 2
        left_border = -1
        right_border = 2
        if row == 0:
            up_border = 0
        if row == self.height - 1:
            down_border = 1
        if col == 0:
            left_border = 0
        if col == self.width - 1:
            right_border = 1

        for row_diff in range(up_border, down_border):  # заполняю список с позициями соседей
            for col_diff in range(left_border, right_border):
                if row_diff == 0 and col_diff == 0:
                    pass
                else:
                    cell_neigbours_pos.append([row + row_diff, col + col_diff])

        alive_neghbours = 0  # считаю живых соседей текущей клетки по позициям из списка
        for pos in cell_neigbours_pos:
            cell_row = pos[0]
            cell_col = pos[1]
            if self.is_alive(cell_row, cell_col):
                alive_neghbours += 1

        # определяю следующее состояние клетки согласно правилам игры
        next_condition = False
        if alive_neghbours <= 1 or alive_neghbours >= 4:
            next_condition = False
        if alive_neghbours in (2, 3) and self.is_alive(row, col):
            next_condition = True
        if alive_neghbours == 3 and not self.is_alive(row, col):
            next_condition = True

        self.next_board[row][col] = next_condition # заполняю вспомогательную доску следующим поколением клеток

    def is_alive(self, row: int, col: int) -> bool:
        return self.board[row][col]

    def next(self) -> None:
        for row in range(0, self.height):
            for col in range(0, self.width):
                self.toggle_cell(row, col)

        self.board = self.next_board

        self.next_board = []
        for _ in range(self.height):
            row = [False] * self.width
            self.next_board.append(row)


if __name__ == "__main__":
    board = Board(3, 3)
    for i in range(0, 3):
        board.place_cell(1, i)

    for i in range(100):
        print(board)
        board.next()
        sleep(0.5)
