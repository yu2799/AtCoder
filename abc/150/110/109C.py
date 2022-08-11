from functools import reduce
from math import gcd
from sys import stdin


def main():
    input = stdin.readline
    _, x = map(int, input().split())
    a = list(map(lambda i: abs(int(i) - x), input().split()))
    print(reduce(gcd, a))


if __name__ == "__main__":
    main()
