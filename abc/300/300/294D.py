from heapq import heappop, heappush
from sys import stdin


def main():
    input = stdin.readline
    _, q = map(int, input().split())
    res = []
    cnt = 1
    hq = []
    tmp = set()
    for _ in range(q):
        event = list(map(int, input().split()))
        if event[0] == 1:
            heappush(hq, cnt)
            cnt += 1
        elif event[0] == 2:
            tmp.add(event[1])
        else:
            while hq and hq[0] in tmp:
                heappop(hq)
            res.append(hq[0])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
