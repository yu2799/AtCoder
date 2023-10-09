from bisect import bisect_right
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(sorted(map(int, input().split())))
    q = int(input())
    res = []
    for _ in range(q):
        b = int(input())
        idx = bisect_right(a, b)
        if idx == 0:
            res.append(abs(a[idx] - b))
        elif idx == n:
            res.append(abs(a[idx - 1] - b))
        else:
            res.append(min(abs(a[idx] - b), abs(a[idx - 1] - b)))
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
