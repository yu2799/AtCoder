from sys import stdin
from array import array
from bisect import bisect_left


def main():
    input = stdin.readline
    l, q = map(int, input().split())
    cut = array("i", [0, l])
    res = []
    for _ in [0] * q:
        c, q = map(int, input().split())
        i = bisect_left(cut, q)
        if c == 1:
            cut.insert(i, q)
        else:
            res.append(cut[i] - cut[i - 1])

    print(*res, sep="\n")


if __name__ == "__main__":
    main()
