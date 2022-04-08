from sys import stdin
from heapq import heappop, heappush


def main():
    input = stdin.readline
    q = int(input())
    tmp = 0
    h = []
    res = []
    for _ in [0] * q:
        query = tuple(map(int, input().split()))
        if query[0] == 1:
            heappush(h, query[1] - tmp)
        elif query[0] == 2:
            tmp += query[1]
        else:
            res.append(heappop(h) + tmp)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
