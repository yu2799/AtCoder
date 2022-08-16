from itertools import accumulate
from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = tuple(map(int, input().split()))
    accm = list(accumulate(a, initial=0))
    print(sum(accm[k:]) - sum(accm[: n - k + 1]))


if __name__ == "__main__":
    main()
