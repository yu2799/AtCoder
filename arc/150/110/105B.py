from sys import stdin
from math import gcd
from functools import reduce


def main():
    input = stdin.readline
    n = int(input())
    a = tuple(set(map(int, input().split())))
    print(reduce(gcd, a))


if __name__ == '__main__':
    main()
