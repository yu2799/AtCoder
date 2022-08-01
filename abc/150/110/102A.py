from math import gcd
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print(2 * n // gcd(2, n))


if __name__ == "__main__":
    main()
