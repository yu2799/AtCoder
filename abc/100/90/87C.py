from sys import stdin
from itertools import accumulate


def main():
    input = stdin.readline
    n = int(input())
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    res = 0
    for i in range(n):
        tmp = sum(a1[: i+1]) + sum(a2[i:n])
        if tmp > res:
            res = tmp
    print(res)


if __name__ == '__main__':
    main()
