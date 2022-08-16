from math import sqrt
from sys import stdin


def main():
    input = stdin.readline
    n, d = map(int, input().split())
    res = 0
    for _ in [0] * n:
        x, y = map(int, input().split())
        if sqrt(x * x + y * y) <= d:
            res = res + 1
    print(res)


if __name__ == "__main__":
    main()
