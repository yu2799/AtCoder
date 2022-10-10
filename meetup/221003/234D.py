from heapq import heappush, heappushpop
from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    hq = []
    for i in range(k):
        heappush(hq, p[i])
    res = [hq[0]]
    for i in range(k, n):
        if hq[0] < p[i]:
            heappushpop(hq, p[i])
        res.append(hq[0])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
