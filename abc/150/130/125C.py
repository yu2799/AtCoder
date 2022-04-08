from sys import stdin
from math import gcd


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    gcd_l = [0] * (n + 1)
    gcd_r = [0] * (n + 1)
    for i in range(n):
        gcd_l[i + 1] = gcd(gcd_l[i], a[i])
        gcd_r[n - 1 - i] = gcd(gcd_r[n - i], a[n - 1 - i])
    res = 0
    for i in range(n):
        tmp = gcd(gcd_l[i], gcd_r[i + 1])
        if res < tmp:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
