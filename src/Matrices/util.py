from collections.abc import Sequence


def check_indexes(size: int, indexes):
    if not type(indexes) == tuple:
        raise TypeError("Invalid index type")
    row, col = indexes
    if not (0 <= row < size) or not (0 <= col < size):
        raise IndexError("Index out of range!")


def arr_str(arr: Sequence, size: None):
    res = ""
    size = size if size else len(arr)
    for i in range(size):
        for j in range(size):
            res += f"{arr[i,j]}\t"
        res += "\n"
    return res
