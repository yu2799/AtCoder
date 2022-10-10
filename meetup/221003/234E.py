from bisect import bisect_left
from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    res = []
    for a in range(1, 10):
        res.append(a)
        for d in range(-9, 10):
            buf = str(a)
            prev = a
            digit = 1
            while 0 <= prev + d <= 9 and digit <= 18:
                prev = prev + d
                buf += str(prev)
                res.append(int(buf))
                digit += 1
    res.sort()
    idx = bisect_left(res, x)
    print(res[idx])


if __name__ == "__main__":
    main()
