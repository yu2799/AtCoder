from bisect import bisect_right
from itertools import accumulate
from sys import stdin


def main():
    input = stdin.readline
    n, m, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    accm = list(accumulate(b, initial=0))
    res = 0
    for i in a:
        idx = bisect_right(b, p - i)
        res += (m - idx) * p
        res += accm[idx] + i * idx
    print(res)


if __name__ == "__main__":
    main()
