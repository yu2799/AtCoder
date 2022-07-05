from sys import stdin
from math import sqrt


def main():
    input = stdin.readline
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in [0] * n]
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            tmp = sqrt((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2)
            if res < tmp:
                res = tmp
    print(res)


if __name__ == "__main__":
    main()
