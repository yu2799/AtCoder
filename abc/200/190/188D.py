from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n, C = map(int, input().split())
    d = defaultdict(int)
    for _ in [0] * n:
        a, b, c = map(int, input().split())
        d[a] += c
        d[b + 1] -= c
    event = [(i, d[i]) for i in sorted(d.keys())]
    tot = 0
    res = 0
    prev = 0
    for i, j in event:
        if C < tot:
            res = res + C * (i - prev)
        else:
            res = res + tot * (i - prev)
        tot = tot + j
        prev = i
    print(res)


if __name__ == "__main__":
    main()
