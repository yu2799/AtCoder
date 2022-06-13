from sys import stdin
from math import sqrt, pow


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [tuple(map(int, input().split())) for _ in [0] * n]
    INF = float("inf")
    res = [INF] * n
    for i in a:
        for j in range(n):
            tmp = sqrt(
                pow(xy[i - 1][0] - xy[j][0], 2)
                + pow(xy[i - 1][1] - xy[j][1], 2)
            )
            if res[j] > tmp:
                res[j] = tmp
    print(max(res))


if __name__ == "__main__":
    main()
