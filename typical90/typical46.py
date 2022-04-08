from sys import stdin
from collections import Counter


def main():
    input = stdin.readline
    n = int(input())
    a = Counter([i % 46 for i in map(int, input().split())])
    b = Counter([i % 46 for i in map(int, input().split())])
    c = Counter([i % 46 for i in map(int, input().split())])
    res = 0

    for i in range(46):
        for j in range(46):
            k = (46 - i - j) % 46
            res += a[i] * b[j] * c[k]
    print(res)


if __name__ == '__main__':
    main()
