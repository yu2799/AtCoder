from sys import stdin
from bisect import bisect


def main():
    input = stdin.readline
    n = int(input())
    a = [-10**10] + sorted(set(map(int, input().split()))) + [10**10]
    q = int(input())
    res = []
    for _ in [0] * q:
        b = int(input())
        idx = bisect(a, b)

        if abs(a[idx] - b) > abs(a[idx-1] - b):
            res.append(abs(b - a[idx-1]))
        else:
            res.append(abs(b - a[idx]))

    print(*res, sep="\n")


if __name__ == '__main__':
    main()
