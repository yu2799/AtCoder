from sys import stdin
from math import sqrt, ceil


def main():
    input = stdin.readline
    r, x, y = map(int, input().split())
    d = sqrt(x * x + y * y)
    if d == r:
        print(1)
    elif d <= r + r:
        print(2)
    else:
        print(ceil(d / r))


if __name__ == "__main__":
    main()
