from sys import stdin
from heapq import heappop, heappush


def main():
    input = stdin.readline
    q = int(input())
    hq = []
    res = []
    cnt = 0
    for _ in [0] * q:
        (*query,) = map(int, input().split())
        if query[0] == 1:
            heappush(hq, query[1] - cnt)
        elif query[0] == 2:
            cnt += query[1]
        else:
            res.append(heappop(hq) + cnt)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
