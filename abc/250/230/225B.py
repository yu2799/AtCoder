from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    n = int(input())
    d = defaultdict(int)
    for _ in [0] * (n - 1):
        a, b = map(int, input().split())
        d[a] += 1
        d[b] += 1
    for i in d:
        if d[i] == (n - 1):
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
