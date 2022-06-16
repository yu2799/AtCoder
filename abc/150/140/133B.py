from sys import stdin
from math import sqrt


def main():
    input = stdin.readline
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in [0] * n]
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if sqrt(
                sum([(x[i][k] - x[j][k]) ** 2 for k in range(d)])
            ).is_integer():
                res += 1
    print(res)


if __name__ == "__main__":
    main()
