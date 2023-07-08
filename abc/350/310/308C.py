from functools import cmp_to_key
from sys import stdin


def cmp(a, b):
    if a[0] * b[1] == b[0] * a[1]:
        return 0
    return -1 if a[0] * b[1] < b[0] * a[1] else 1


def main():
    input = stdin.readline
    n = int(input())
    res = []
    for i in range(n):
        a, b = map(int, input().split())
        res.append((a, a + b, i + 1))
    res = sorted(res, reverse=True, key=cmp_to_key(cmp))
    for _, _, i in res:
        print(i, end=" ")


if __name__ == "__main__":
    main()
