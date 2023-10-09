from math import asin, cos, degrees, pi, sin, sqrt
from sys import stdin


def main():
    input = stdin.readline
    t = int(input())
    l, x, y = map(int, input().split())
    q = int(input())
    res = []
    for _ in [0] * q:
        e = int(input())
        a = -l / 2 * sin(2 * pi * e / t)
        b = -l / 2 * (cos(2 * pi * e / t) - 1)
        res.append(degrees(asin(b / sqrt(x * x + (y - a) * (y - a) + b * b))))

    print(*res, sep="\n")


if __name__ == "__main__":
    main()
