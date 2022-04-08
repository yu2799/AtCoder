from sys import stdin
from itertools import product


def main():
    input = stdin.readline
    n, x = map(int, input().split())
    a = []
    for _ in [0] * n:
        l = [int(i) for i in input().split()]
        a.append(l[1:])
    prod = product(*a)
    res = 0
    for i in prod:
        tmp = 1
        for j in i:
            tmp *= j
        if tmp == x:
            res += 1
    print(res)


if __name__ == '__main__':
    main()
