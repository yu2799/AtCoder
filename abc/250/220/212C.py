from sys import stdin
from bisect import bisect_right


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    res = 10 ** 9
    for i in a:
        idx = bisect_right(b, i)
        if idx == 0:
            res = min(abs(b[idx] - i), res)
        elif idx == m:
            res = min(abs(b[idx - 1] - i), res)
        else:
            res = min(min(abs(b[idx] - i), abs(b[idx - 1] - i)), res)

    else:
        print(res)


if __name__ == "__main__":
    main()
