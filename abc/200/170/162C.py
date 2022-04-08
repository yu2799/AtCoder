from sys import stdin
from math import gcd


def main():
    input = stdin.readline
    k = int(input())
    res = 0
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            tmp = gcd(i, j)
            for k in range(1, k + 1):
                res += gcd(tmp, k)
    print(res)


if __name__ == "__main__":
    main()
