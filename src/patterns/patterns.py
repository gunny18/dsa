def pattern1(n: int):
    """
    * * *
    * * *
    * * *
    """

    for _ in range(n):
        for _ in range(n):
            print("* ", end="")
        print("\n", end="")


def pattern2(n: int):
    """
    *
    * *
    * * *
    * * * *
    """

    for i in range(n):
        for _ in range(i + 1):
            print("* ", end="")
        print("\n", end="")


def pattern3(n: int):
    """
    1
    1 2
    1 2 3
    1 2 3 4
    """

    for i in range(n):
        for j in range(i + 1):
            print(j + 1, " ", end="")
        print("\n", end="")


def pattern4(n: int):
    """
    1
    2 2
    3 3 3
    4 4 4 4
    """

    for i in range(n):
        for _ in range(i + 1):
            print(i + 1, " ", end="")
        print("\n", end="")


def pattern5(n: int):
    """
    * * * * *
    * * * *
    * * *
    * *
    *
    """

    for i in range(1, n + 1):
        for _ in range(1, (n - i + 1) + 1):
            print("* ", end="")
        print("\n", end="")


def pattern6(n: int):
    """
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
    """

    for i in range(1, n + 1):
        for j in range(1, (n - i + 1) + 1):
            print(j, " ", end="")
        print("\n", end="")


def pattern7(n: int):
    """
        *
      * * *
    * * * * *
    """

    for i in range(n):
        for _ in range(n - i - 1):
            print("  ", end="")
        for _ in range(2 * i + 1):
            print("* ", end="")
        for _ in range(n - i - 1):
            print("  ", end="")
        print("\n", end="")


def pattern8(n: int):
    """
        *
      * * *
    * * * * *
    (reversed version of this)
    """

    for i in range(n):
        for _ in range(i):
            print("  ", end="")
        for _ in range(2 * n - 2 * i - 1):
            print("* ", end="")
        for _ in range(i):
            print("  ", end="")
        print("\n", end="")


def pattern9(n: int):
    """
    Double sided pyramid - combo of pattern 7 and 8
    """
    pattern7(n)
    pattern8(n)


def pattern10(n: int):
    """
    n = 4
    *
    * *
    * * *
    * * * *
    * * *
    * *
    *
    """
    for i in range(2 * n - 1):
        stars = i + 1
        if i >= n:
            stars = 2 * n - i - 1
        for _ in range(stars):
            print("* ", end="")
        print("\n", end="")


def pattern11(n: int):
    """
    n=4
    1
    0 1
    1 0 1
    0 1 0 1
    """
    start = 1
    for i in range(n):
        start = 1 if i % 2 == 0 else 0
        for _ in range(i + 1):
            print(start, " ", end="")
            start = 1 - start
        print("\n", end="")


def pattern12(n: int):
    """
    n = 4
    1             1
    1 2         2 1
    1 2 3     3 2 1
    1 2 3 4 4 3 2 1
    """
    for i in range(n):
        # number
        for val in range(i + 1):
            print(val + 1, end="")
        # space
        space = 2 * (n - i - 1)
        for _ in range(space):
            print(" ", end="")
        # number - reversed order
        for val in range(i + 1, 0, -1):
            print(val, end="")
        print("\n", end="")


def pattern13(n: int):
    """
    1
    2 3
    4 5 6
    7 8 9 10
    """
    count = 1
    for i in range(n):
        for _ in range(i + 1):
            print(count, " ", end="")
            count += 1
        print("\n", end="")


def pattern14(n: int):
    for i in range(n):
        start = "A"
        for j in range(i + 1):
            print(chr(ord(start) + j), " ", end="")
        print("\n", end="")


def pattern15(n: int):
    """
    A B C D
    A B C
    A B
    A
    """
    for i in range(n):
        start = "A"
        for j in range(n - i):
            print(chr(ord(start) + j), " ", end="")
        print("\n", end="")


def pattern16(n: int):
    """
    A A A A
    B B B
    C C
    D
    """
    for i in range(n):
        start = "A"
        for _ in range(i + 1):
            val = chr(ord(start) + i)
            print(val, " ", end="")
        print("\n", end="")


def pattern17(n: int):
    """
    n=4
       A
      ABA
     ABCBA
    ABCDCBA
    """
    for i in range(n):
        start = "A"
        spaces = n - i - 1
        for _ in range(spaces):
            print(" ", end="")
        for j in range(2 * i + 1):
            start = chr(ord(start) + j) if j <= i else chr(ord(start) - 1)
            print(start, end="")
        for _ in range(spaces):
            print(" ", end="")
        print("\n", end="")


if __name__ == "__main__":
    n = int(input("Value: "))
    pattern17(n)
