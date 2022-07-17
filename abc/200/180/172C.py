from sys import stdin
from itertools import accumulate
from bisect import bisect_right


def main():
    input = stdin.readline
    _, _, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_accum = list(accumulate(a, initial=0))
    b_accum = list(accumulate(b, initial=0))
    res = 0
    for i, j in enumerate(a_accum):
        if i > k:
            break
        idx = bisect_right(b_accum, k - j)
        if b_accum[idx - 1] + j <= k and res < i + idx - 1:
            res = i + idx - 1
    print(res)


if __name__ == "__main__":
    main()
