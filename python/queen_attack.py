class Queen:
    def __init__(self, row: int, column: int):
        if row < 0:
            raise ValueError("row not positive")
        elif row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        elif column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.column = column

    def can_attack(self, another_queen: object) -> bool:
        """Return True if a queen can attack another queen."""
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError(
                "Invalid queen position: both queens in the same square")
        elif self.row == another_queen.row or self.column == another_queen.column:
            return True
        for n in range(1, 7):
            if another_queen.row == self.row + n or another_queen.row == self.row - n:
                if another_queen.column == self.column + n or another_queen.column == self.column - n:
                    return True
        return False


# 2, 6 ==> 3, 5 | 4, 4

black = Queen(2, 2)
# white = Queen(0, 4)


print(black.can_attack(white))
