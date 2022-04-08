from sys import stdin
from math import sqrt


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    c = sqrt(a * a + b * b)
    print(a / c, b / c)


if __name__ == "__main__":
    main()
