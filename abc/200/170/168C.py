from math import cos, pi, sqrt
from sys import stdin


def main():
    input = stdin.readline
    a, b, h, m = map(int, input().split())
    print(
        sqrt(
            a * a
            + b * b
            - 2 * a * b * cos((h + m / 60) / 6 * pi - m / 30 * pi)
        )
    )


if __name__ == "__main__":
    main()
