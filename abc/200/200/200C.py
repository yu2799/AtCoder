from sys import stdin
from collections import Counter


def main():
    input = stdin.readline
    n = int(input())
    a = [i % 200 for i in map(int, input().split())]
    c = Counter(a)
    res = 0
    for i in c.values():
        res = res + i * (i - 1) // 2
    print(res)


if __name__ == "__main__":
    main()
