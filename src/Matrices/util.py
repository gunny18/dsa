from collections.abc import Sequence


def arr_str(arr: Sequence):
    res = ""
    size = len(arr)
    for i in range(size):
        for j in range(size):
            res += f"{arr[i,j]}\t"
        res += "\n"
    return res
