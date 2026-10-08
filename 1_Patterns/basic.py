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


def p9(n):
    # Upper half
    p7(n)
    # Lower half
    p8(n)


def p10(n):
    for i in range(1, n + 1):
        for _ in range(i):
            print("*", end="")

        for _ in range(n - i):
            print(" ", end="")

        print()

    for i in range(n - 1, 0, -1):
        for _ in range(i):
            print("*", end="")

        for _ in range(n - i):
            print(" ", end="")

        print()


def p11(n):
    for i in range(1, n + 1):
        bit = 1
        if i % 2 == 0:
            bit = 0
        for _ in range(i):
            print(bit, end="")
            bit = 1 - bit

        print()


def p12(n):
    for i in range(1, n + 1):
        # fwd range
        for j in range(1, i + 1):
            print(j, end="")

        # Space
        for _ in range(2 * n - 2 * i):
            print(" ", end="")

        # bckws range
        for j in range(i, 0, -1):
            print(j, end="")

        print()


def p13(n):
    cnt = 1
    for i in range(1, n + 1):
        for _ in range(i):
            print(cnt, end="")
            cnt += 1

        for _ in range(n - i):
            print(" ", end="")

        print()


def p14(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(ord("A") + j), end="")

        print()


def p15(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(ord("A") + j), end="")
        print()


def p16(n):
    for i in range(1, n + 1):
        for _ in range(i):
            print(chr(ord("A") + i - 1), end="")
        print()


def p17(n):
    for i in range(1, n + 1):
        for _ in range(n - i):
            print(" ", end="")

        for j in range(i):
            print(chr(ord("A") + j), end="")

        for k in range(i - 1):
            print(chr(ord("A") + j - k - 1), end="")

        for _ in range(n - i):
            print(" ", end="")

        print()


def p18(n):
    for i in range(1, n + 1):
        st = chr(ord("A") + n - i)
        for j in range(i):
            print(chr(ord(st) + j), end="")
        print()


def p19(n):
    for i in range(n, 0, -1):
        for _ in range(i):
            print("*", end="")

        for _ in range(2 * n - 2 * i):
            print(" ", end="")

        for _ in range(i):
            print("*", end="")

        print()

    for i in range(1, n + 1):
        for _ in range(i):
            print("*", end="")

        for _ in range(2 * n - 2 * i):
            print(" ", end="")

        for _ in range(i):
            print("*", end="")

        print()


def p20(n):
    for i in range(1, n + 1):
        for _ in range(i):
            print("*", end="")

        for _ in range(2 * n - 2 * i):
            print(" ", end="")

        for _ in range(i):
            print("*", end="")

        print()

    for i in range(n - 1, 0, -1):
        for _ in range(i):
            print("*", end="")

        for _ in range(2 * n - 2 * i):
            print(" ", end="")

        for _ in range(i):
            print("*", end="")

        print()


def p21(n):
    for i in range(1, n + 1):
        if i in (1, n):
            for _ in range(n):
                print("*", end="")
        else:
            for j in range(1, n + 1):
                if j in (1, n):
                    print("*", end="")
                else:
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
    print("===========")
    p9(4)
    print("===========")
    p10(4)
    print("===========")
    p11(5)
    print("===========")
    p12(5)
    print("===========")
    p13(5)
    print("===========")
    p14(5)
    print("===========")
    p15(5)
    print("===========")
    p16(5)
    print("===========")
    p17(5)
    print("===========")
    p18(5)
    print("===========")
    p19(5)
    print("===========")
    p20(5)
    print("===========")
    p21(5)
