from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    n = int(input())
    d = defaultdict(int)
    xy = [tuple(map(int, input().split())) for _ in [0] * n]
    res = []
    for x, y in xy:
        d[x] += 1
        d[y] -= 1
    key = sorted(d.keys())
    res = []
    cnt = 0
    for i in key:
        if cnt == 0:
            s = i
        cnt += d[i]
        if cnt == 0:
            res.append((s, i))
    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
