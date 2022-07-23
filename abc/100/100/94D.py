from sys import stdin
from bisect import bisect_right


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    a.sort()
    left = a[-1]
    idx = bisect_right(a, left / 2)
    right = (
        a[idx - 1]
        if abs(a[idx - 1] - left / 2) <= abs(a[idx] - left / 2)
        else a[idx]
    )
    print(left, right)


if __name__ == "__main__":
    main()
