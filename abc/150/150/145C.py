from sys import stdin
from itertools import permutations
from math import sqrt


def main():
    input = stdin.readline
    n = int(input())
    xy = []
    for _ in [0] * n:
        x, y = map(int, input().split())
        xy.append((x, y))
    permutation = list(permutations(range(n)))
    res = 0
    cnt = 0
    for i in permutation:
        cnt += 1
        prev = i[0]
        for j in i[1:]:
            res += sqrt((xy[prev][0] - xy[j][0]) ** 2 + (xy[prev][1] - xy[j][1]) ** 2)
    print(res / cnt)


if __name__ == "__main__":
    main()
