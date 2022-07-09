from sys import stdin
from math import sin, cos, pi


def main():
    input = stdin.readline
    a, b, d = map(int, input().split())
    print(
        a * cos(d / 180 * pi) - b * sin(d / 180 * pi),
        a * sin(d / 180 * pi) + b * cos(d / 180 * pi),
    )


if __name__ == "__main__":
    main()
