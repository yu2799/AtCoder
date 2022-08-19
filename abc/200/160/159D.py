from collections import Counter
from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    d = Counter(a)
    tmp = sum([i * (i - 1) // 2 for i in d.values()])
    res = [tmp - d[i] + 1 for i in a]
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
