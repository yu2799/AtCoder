from sys import stdin
from collections import Counter


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    c = Counter(a)
    res = 0
    for i in range(10 ** 5):
        tmp = c[i] + c[i + 1] + c[i + 2]
        if res < tmp:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
