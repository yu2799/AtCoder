from heapq import heappop, heappush
from sys import stdin


def dijkstra(n, start, graph):
    d = [float("inf")] * n
    d[start] = 0
    visited = [False] * n
    hq = [(0, start)]
    while hq:
        _, u = heappop(hq)
        if visited[u]:
            continue
        visited[u] = True
        for v, cost in graph[u]:
            if d[v] > d[u] + cost:
                d[v] = d[u] + cost
                heappush(hq, (d[v], v))
    return d


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    g = [[] for _ in [0] * n]
    for _ in [0] * m:
        u, v = map(lambda x: int(x) - 1, input().split())
        if h[u] < h[v]:
            u, v = v, u
        g[u].append((v, 0))
        g[v].append((u, h[u] - h[v]))
    dist = dijkstra(n, 0, g)
    res = 0
    for i in range(n):
        tmp = -(h[i] + dist[i] - h[0])
        if res < tmp:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
