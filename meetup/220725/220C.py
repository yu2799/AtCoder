from sys import stdin
from itertools import accumulate
from bisect import bisect_right


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    accm = list(accumulate(a))
    print((x // accm[-1]) * n + bisect_right(accm, x % accm[-1]) + 1)


if __name__ == "__main__":
    main()
