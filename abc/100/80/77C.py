from sys import stdin
from bisect import bisect_left, bisect_right


def main():
    input = stdin.readline
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    c = sorted(list(map(int, input().split())))
    res = 0

    for i in b:
        l = bisect_left(a, i)
        r = n - bisect_right(c, i)
        res += l * r

    print(res)


if __name__ == '__main__':
    main()
