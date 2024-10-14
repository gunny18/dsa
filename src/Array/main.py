def shiftLeft(arr: list, n=1) -> list:
    idx = 0
    while idx < len(arr):
        if n >= len(arr):
            arr[idx] = 0
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


def main():
    l = [1, 2, 3, 4, 5]
    shiftRight(l, 10)
    print(l)


if __name__ == "__main__":
    main()
