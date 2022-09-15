from math import factorial
from sys import stdin


def main():
    input = stdin.readline
    L = int(input())
    print(factorial(L - 1) // factorial(11) // factorial(L - 12))


if __name__ == "__main__":
    main()
