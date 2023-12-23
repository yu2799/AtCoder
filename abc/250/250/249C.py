from collections import defaultdict
from itertools import product
from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    s = [input()[:-1] for _ in range(n)]
    res = 0
    for per in list(product((0, 1), repeat=n)):
        d = defaultdict(int)
        for idx, i in enumerate(per):
            if i != 0:
                continue
            for j in s[idx]:
                d[j] += 1
        res = max(res, sum(1 for i in d.values() if i == k))
    print(res)


if __name__ == "__main__":
    main()
