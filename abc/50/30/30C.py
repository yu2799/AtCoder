from bisect import bisect_left
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0
    cur = 0
    while True:
        ai = bisect_left(a, cur)
        if ai == n:
            break
        cur = a[ai] + x
        bi = bisect_left(b, cur)
        if bi == m:
            break
        cur = b[bi] + y
        res += 1
    print(res)


if __name__ == "__main__":
    main()
