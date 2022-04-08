from sys import stdin
from math import gcd


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    res = a // gcd(a, b) * b
    if res > 10 ** 18:
        print("Large")
    else:
        print(res)


if __name__ == '__main__':
    main()
