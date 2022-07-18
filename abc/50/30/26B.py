from sys import stdin
from math import pi


def main():
    input = stdin.readline
    n = int(input())
    r = sorted([int(input()) for _ in [0] * n], reverse=True)
    print(
        sum([i * i if idx % 2 == 0 else -i * i for idx, i in enumerate(r)])
        * pi
    )


if __name__ == "__main__":
    main()
