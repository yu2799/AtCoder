from bisect import bisect_left, bisect_right
from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(list)
    for idx, i in enumerate(a):
        d[i].append(idx)
    res = []
    q = int(input())
    for _ in [0] * q:
        left, right, x = map(int, input().split())
        left -= 1
        right -= 1
        l_idx = bisect_left(d[x], left)
        r_idx = bisect_right(d[x], right)
        res.append(r_idx - l_idx)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
