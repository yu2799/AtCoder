from sys import stdin
from heapq import heappush, heappushpop


def main():
    input = stdin.readline
    _, k = map(int, input().split())
    p = list(map(int, input().split()))
    hq = []
    for i in p[:k]:
        heappush(hq, i)
    res = [hq[0]]
    for i in p[k:]:
        if hq[0] < i:
            heappushpop(hq, i)
        res.append(hq[0])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
