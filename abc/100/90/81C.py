from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    _, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    print(sum(sorted(d.values(), reverse=True)[k:]))


if __name__ == "__main__":
    main()
