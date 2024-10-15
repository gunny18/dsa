from util import arr_str, check_indexes
from lower_triangular import LowerTriangle


class Symmetric(LowerTriangle):
    def __init__(self, size=4):
        super().__init__(size=size)

    def __repr__(self):
        return arr_str(self, self.size)

    def __len__(self):
        return len(self.array)

    def _row_major(self, i, j):
        return ((i * (i + 1)) // 2) + j

    def _col_major(self, i, j):
        return (j * self.size) - ((j * (j - 1)) // 2) + (i - j)

    def __getitem__(self, indexes):
        check_indexes(self.size, indexes)
        row, col = indexes
        if row < col:
            row, col = col, row
        # index = self._row_major(row, col)
        index = self._col_major(row, col)
        return self.array[index]

    def __setitem__(self, indexes, value):
        check_indexes(self.size, indexes)
        row, col = indexes
        if col > row:
            row, col = col, row
        index = self._row_major(row, col)
        self.array[index] = value


if __name__ == "__main__":
    t = Symmetric()
    print(t)
