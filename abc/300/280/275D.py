from collections import defaultdict
from sys import stdin


def calc(n, d):
    if n == 0:
        return 1
    elif d[n] == 0:
        d[n] = calc(n // 2, d) + calc(n // 3, d)
    return d[n]


def main():
    input = stdin.readline
    n = int(input())
    d = defaultdict(int)
    print(calc(n, d))


if __name__ == "__main__":
    main()
