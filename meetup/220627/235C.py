from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(list)
    for idx, i in enumerate(a):
        d[i].append(idx + 1)

    res = []
    for _ in [0] * q:
        x, k = map(int, input().split())
        if k <= len(d[x]):
            res.append(d[x][k - 1])
        else:
            res.append(-1)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
