from math import gcd
from sys import stdin


def lcm(x, y):
    return x // gcd(x, y) * y


def main():
    input = stdin.readline
    n = int(input())
    res = 1
    for i in range(2, n + 1):
        res = lcm(res, i)
    print(res + 1)


if __name__ == "__main__":
    main()
