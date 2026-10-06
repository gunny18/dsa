def p1(n):
    for _ in range(n):
        for _ in range(n):
            print("*", end="")
        print()


def p2(n):
    for i in range(n):
        for _ in range(i + 1):
            print("*", end="")
        print()


def p3(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end="")
        print()


def p4(n):
    for i in range(n):
        for _ in range(i + 1):
            print(i + 1, end="")
        print()


def p5(n):
    for i in range(n, -1, -1):
        for _ in range(i):
            print("*", end="")
        print()


def p6(n):
    for i in range(n, -1, -1):
        for j in range(i):
            print(j + 1, end="")
        print()


def p7(n):
    for i in range(1, n + 1):
        for _ in range(n - i):
            print(" ", end="")

        for _ in range(2 * i - 1):
            print("*", end="")

        for _ in range(n - i):
            print(" ", end="")

        print()


def p8(n):
    for i in range(n, 0, -1):
        for _ in range(n - i):
            print(" ", end="")

        for _ in range(2 * i - 1):
            print("*", end="")

        for _ in range(n - i):
            print(" ", end="")

        print()


if __name__ == "__main__":
    p1(4)
    print("===========")
    p2(4)
    print("===========")
    p3(4)
    print("===========")
    p4(4)
    print("===========")
    p5(4)
    print("===========")
    p6(4)
    print("===========")
    p7(4)
    print("===========")
    p8(4)
