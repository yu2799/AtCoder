from itertools import permutations
from math import sqrt
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in [0] * n]
    per = list(permutations(list(range(n))))
    res = 0
    for i in per:
        for j in range(n - 1):
            res += sqrt(
                (xy[i[j]][0] - xy[i[j + 1]][0]) ** 2
                + (xy[i[j]][1] - xy[i[j + 1]][1]) ** 2
            )
    print(res / len(per))


if __name__ == "__main__":
    main()
