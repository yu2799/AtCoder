from sys import stdin
from itertools import accumulate


def main():
    input = stdin.readline
    n, m, k = map(int, input().split())
    a = [i for i in map(int, input().split())]
    b = [i for i in map(int, input().split())]
    a_accum = list(accumulate(a, initial=0))
    b_accum = list(accumulate(b, initial=0))
    res = 0
    tmp = m
    for i in range(n + 1):
        if a_accum[i] > k:
            break

        while a_accum[i] + b_accum[tmp] > k:
            tmp -= 1
        else:
            if res < i + tmp:
                res = i + tmp

    print(res)


if __name__ == "__main__":
    main()
