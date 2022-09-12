from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    p = list(map(int, input().split()))
    d = defaultdict(int)
    res = 0
    for i in [(i - idx) % n for idx, i in enumerate(p)]:
        d[i] += 1
    for i in range(n):
        tmp = d[(i - 1) % n] + d[i % n] + d[(i + 1) % n]
        if res < tmp:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
