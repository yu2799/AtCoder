from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    n = int(input())
    d = defaultdict(int)
    res = [0] * (n + 1)
    for _ in [0] * n:
        a, b = map(int, input().split())
        d[a] += 1
        d[a + b] -= 1
    a = sorted(d.keys())
    prev = 0
    cur = 0
    for i in a:
        res[cur] += i - prev
        cur += d[i]
        prev = i
    print(*res[1:])


if __name__ == "__main__":
    main()
