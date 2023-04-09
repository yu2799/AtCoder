from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    res = []
    d = defaultdict(int)
    for _ in range(q):
        a, x = map(int, input().split())
        if a != 3:
            d[x] += a
        else:
            res.append("Yes" if d[x] >= 2 else "No")
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
