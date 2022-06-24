from sys import stdin
from math import gcd


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))


if __name__ == "__main__":
    main()
