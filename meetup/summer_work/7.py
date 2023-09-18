from heapq import heappop, heappush
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    p = map(int, input().split())
    res = []
    tmp = 0
    hq = []
    for i in p:
        if i == tmp:
            tmp += 1
            while hq and tmp == hq[0]:
                tmp += 1
                heappop(hq)
            res.append(tmp)
        elif tmp < i:
            res.append(tmp)
            heappush(hq, i)
        else:
            res.append(tmp)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
