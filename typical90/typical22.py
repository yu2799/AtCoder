from math import gcd
from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    tmp = gcd(a, b, c)
    print(a // tmp + b // tmp + c // tmp - 3)


if __name__ == "__main__":
    main()
