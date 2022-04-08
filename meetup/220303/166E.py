from sys import stdin
from collections import Counter


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    b = Counter([i + 1 - j for i, j in enumerate(a)])
    c = Counter([i + 1 + j for i, j in enumerate(a)])
    res = 0
    for i in range(n, 0, -1):
        res += b[i + a[i - 1]]
        res += c[i - a[i - 1]]
    print(res // 2)


if __name__ == "__main__":
    main()
