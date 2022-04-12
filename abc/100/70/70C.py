from sys import stdin
from math import gcd


def main():
    input = stdin.readline
    n = int(input())
    res = 1
    for _ in [0] * n:
        tmp = int(input())
        res = res // gcd(res, tmp) * tmp
    print(res)


if __name__ == '__main__':
    main()
