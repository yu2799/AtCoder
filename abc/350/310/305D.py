from bisect import bisect_left
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    acc = [0] * ((n + 1) // 2)
    for i in range(n // 2):
        acc[i + 1] = acc[i] + a[i * 2 + 2] - a[i * 2 + 1]
    q = int(input())
    res = [0] * q
    for i in range(q):
        left, right = map(int, input().split())
        l_idx = bisect_left(a, left)
        r_idx = bisect_left(a, right)
        tmp = 0
        if l_idx % 2 == 0:
            tmp = tmp + (a[l_idx] - left)
        if r_idx % 2 == 0:
            tmp = tmp + (right - a[r_idx - 1])
        res[i] = tmp + acc[(r_idx - 1) // 2] - acc[l_idx // 2]
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
