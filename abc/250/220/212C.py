from sys import stdin
from bisect import bisect_right


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    res = 10**9
    for i in a:
        idx = bisect_right(b, i)
        if idx == 0:
            diff = b[idx] - i
        elif idx == m:
            diff = i - b[idx - 1]
        else:
            diff = min(i - b[idx - 1], b[idx] - i)
        if diff < res:
            res = diff
    print(res)


if __name__ == "__main__":
    main()
