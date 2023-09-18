from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    res = 0
    cnt = 0
    d = defaultdict(int)
    for i in range(k):
        if d[c[i]] == 0:
            cnt += 1
        d[c[i]] += 1

    res = cnt
    for i in range(k, n):
        d[c[i - k]] -= 1
        if d[c[i - k]] == 0:
            cnt -= 1
        if d[c[i]] == 0:
            cnt += 1
        d[c[i]] += 1
        res = max(res, cnt)
    print(res)


if __name__ == "__main__":
    main()
