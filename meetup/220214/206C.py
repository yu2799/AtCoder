from sys import stdin
from collections import Counter


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    c = Counter(a)
    res = n * (n - 1) // 2
    for i in c.values():
        res = res - i * (i - 1) // 2
    print(res)


if __name__ == "__main__":
    main()
