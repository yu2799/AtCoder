from math import sqrt
from sys import stdin


def f(num, a, b):
    return b * num + a / sqrt(num + 1)


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    left = 0
    right = 10**18
    while left + 2 < right:
        c1 = left + (right - left) // 3
        c2 = right - (right - left) // 3
        if f(c1, a, b) < f(c2, a, b):
            right = c2
        else:
            left = c1

    print(min(f(left, a, b), f(left + 1, a, b), f(right, a, b)))


if __name__ == "__main__":
    main()
