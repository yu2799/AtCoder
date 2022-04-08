from sys import stdin
from heapq import heappop, heappush
from collections import deque


def main():
    input = stdin.readline
    q = int(input())
    heap = []
    d = deque()
    res = []
    for _ in [0] * q:
        query = [int(i) for i in input().split()]
        if query[0] == 1:
            d.append(query[1])
        elif query[0] == 2:
            res.append(heappop(heap) if heap else d.popleft())
        else:
            while d:
                heappush(heap, d.pop())
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
