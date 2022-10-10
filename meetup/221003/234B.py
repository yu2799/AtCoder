from math import sqrt
from sys import stdin


def dis(s, t):
    return sqrt((s[0] - t[0]) ** 2 + (s[1] - t[1]) ** 2)


def main():
    input = stdin.readline
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in [0] * n]
    res = 0
    for s in xy:
        for t in xy:
            tmp = dis(s, t)
            if res < tmp:
                res = tmp
    print(res)


if __name__ == "__main__":
    main()
