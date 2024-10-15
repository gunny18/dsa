from util import arr_str


class Diagonal:
    def __init__(self, values: list) -> None:
        self.array = values

    def _check_indexes(self, row: int):
        if not (0 <= row < len(self.array)):
            raise IndexError("Index out of range")

    def __repr__(self):
        return arr_str(self)

    def __len__(self):
        return len(self.array)

    def __getitem__(self, indexes):
        if type(indexes) == int:
            row = indexes
            col = row
        elif type(indexes) == tuple:
            row, col = indexes
        else:
            raise IndexError("Invalid Index type")
        self._check_indexes(row)
        if row != col:
            return 0
        return self.array[row]

    def __setitem__(self, indexes, value):
        if type(indexes) == int:
            row = indexes
            col = row
        elif type(indexes) == tuple:
            row, col = indexes
        else:
            raise IndexError("Invalid Index type")
        self._check_indexes(row)
        if row != col:
            raise IndexError("Cannot set values for non diagonal indexes")
        self.array[row] = value


if __name__ == "__main__":
    d = Diagonal([1, 2, 3, 4, 5])
    print(d[4])
    d[4] = 10
    print(d[4])
    d[0, 0] = -1
    print(d[0])
    print(d)
