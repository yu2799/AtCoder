from sys import stdin
from itertools import permutations


def main():
    input = stdin.readline
    n = int(input())
    a = [list(map(int, input().split())) for _ in [0] * n]
    m = int(input())
    xy = set()
    for _ in [0] * m:
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        xy.add((x, y))
        xy.add((y, x))
    patterns = list(permutations(range(n)))
    res = -1

    for pattern in patterns:
        tmp = a[pattern[0]][0]
        prev = pattern[0]
        for i in range(1, n):
            if (prev, pattern[i]) in xy:
                break
            tmp += a[pattern[i]][i]
            prev = pattern[i]
        else:
            if res == -1 or res > tmp:
                res = tmp
    print(res)


if __name__ == '__main__':
    main()
