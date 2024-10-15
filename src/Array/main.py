def shiftLeft(arr: list, n=1) -> list:
    idx = 0
    while idx < len(arr):
        if n >= len(arr):
            arr[idx] = 0
        else:
            arr[idx] = arr[n]
            n += 1
        idx += 1


def rotateLeft(arr: list, n=1) -> list:
    idx = 0
    temp = []
    while idx < len(arr):
        temp.append(arr[idx])
        if n >= len(arr):
            arr[idx] = temp.pop(0)
        else:
            arr[idx] = arr[n]
            n += 1
        idx += 1


def shiftRight(arr: list, n=1):
    idx = len(arr) - 1
    n = len(arr) - n - 1
    while idx >= 0:
        if n < 0:
            arr[idx] = 0
        else:
            arr[idx] = arr[n]
            n -= 1
        idx -= 1


def rotateRight(arr: list, n=1):
    idx = len(arr) - 1
    n = len(arr) - n - 1
    temp = []
    while idx >= 0:
        temp.append(arr[idx])
        if n < 0:
            arr[idx] = temp.pop(0)
        else:
            arr[idx] = arr[n]
            n -= 1
        idx -= 1


def insertInSortedArray(arr: list, element):
    idx = 0
    while idx < len(arr):
        if arr[idx] > element:
            break
        idx += 1
    arr.insert(idx, element)


def checkIfSorted(arr: list):
    idx = 0
    while idx < len(arr) - 1:
        if arr[idx] > arr[idx + 1]:
            return False
        idx += 1
    return True


def arrangeNegPos(arr: list):
    i = 0
    j = len(arr) - 1
    while i < j:
        while arr[i] < 0:
            i += 1
        while arr[j] >= 0:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def main():
    l = [1, -1, 2, 3, -4, -5, 10, -11]
    arrangeNegPos(l)
    print(l)


if __name__ == "__main__":
    main()
