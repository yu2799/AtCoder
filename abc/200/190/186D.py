from itertools import accumulate
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    accm = list(accumulate(a, initial=0))
    res = 0
    for i in range(n):
        res += accm[-1] - accm[i] - (n - i) * a[i]

    print(res)


if __name__ == "__main__":
    main()
