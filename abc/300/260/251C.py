from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    n = int(input())
    d = defaultdict(int)
    tmp = 0
    res = 0
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if d[s] != 0:
            continue
        d[s] = t
        if tmp < t:
            tmp = t
            res = i
    print(res + 1)


if __name__ == '__main__':
    main()
