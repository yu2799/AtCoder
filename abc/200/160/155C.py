from sys import stdin
from collections import Counter


def main():
    input = stdin.readline
    n = int(input())
    c = Counter([input()[:-1] for _ in range(n)])
    m = max(c.values())
    keys = sorted([k for k, v in c.items() if m == v])
    print(*keys, sep="\n")


if __name__ == '__main__':
    main()
