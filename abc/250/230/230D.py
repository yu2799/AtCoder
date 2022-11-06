from operator import itemgetter
from sys import stdin


def main():
    input = stdin.readline
    n, d = map(int, input().split())
    lr = [tuple(map(int, input().split())) for _ in [0] * n]
    lr.sort(key=itemgetter(1))
    res = 0
    x = -float("inf")
    for left, right in lr:
        if x + d - 1 < left:
            res = res + 1
            x = right
    print(res)


if __name__ == "__main__":
    main()
