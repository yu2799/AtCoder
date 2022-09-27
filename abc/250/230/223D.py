from heapq import heappop, heappush
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    link = [0] * n
    g = [[] for _ in [0] * n]
    res = []
    for _ in [0] * m:
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)
        link[b] += 1

    q = []
    for i in range(n):
        if link[i] == 0:
            heappush(q, i)
    while q:
        rm = heappop(q)
        res.append(rm + 1)
        for i in g[rm]:
            link[i] -= 1
            if link[i] == 0:
                heappush(q, i)
    if len(res) == n:
        print(*res)
    else:
        print(-1)


if __name__ == "__main__":
    main()
