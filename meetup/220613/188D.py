from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    n, c = map(int, input().split())
    d = defaultdict(int)
    res = 0
    for _ in [0] * n:
        a, b, cost = map(int, input().split())
        b += 1
        d[a] += cost
        d[b] -= cost
    key = sorted(d.keys())

    res = 0
    cur = 0
    tmp = 0
    for i in key:
        res += min(c, tmp) * (i - cur)
        cur = i
        tmp += d[i]
    print(d)
    print(res)


if __name__ == "__main__":
    main()
