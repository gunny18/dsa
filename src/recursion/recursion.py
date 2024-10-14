def sum_of_n_natural_numbers(n: int):
    """
    result = sum(n-1) + sum(n)
    """
    if n == 0:
        return 0
    return sum_of_n_natural_numbers(n - 1) + n


def factorial(n: int):
    if n == 0:
        return 1
    return factorial(n - 1) * n


def main():
    # print(sum_of_n_natural_numbers(10))
    print(factorial(5))


if __name__ == "__main__":
    main()
