from math import gcd
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n - 1):
        res = gcd(res, abs(a[i] - a[i + 1]))
    print(2 if res == 1 else 1)


if __name__ == "__main__":
    main()
