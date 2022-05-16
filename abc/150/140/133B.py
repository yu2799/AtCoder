from sys import stdin
from math import sqrt


def main():
    input = stdin.readline
    n, d = map(int, input().split())
    res = 0
    x = []
    for _ in [0] * n:
        tmp = list(map(int, input().split()))
        x.append(tmp)
    for i in range(n):
        for j in range(i + 1, n):
            if not sqrt(sum([(x[i][k] - x[j][k]) ** 2 for k in range(d)])) % 1:
                res += 1
    print(res)


if __name__ == "__main__":
    main()
