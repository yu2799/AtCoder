from collections import deque
from sys import stdin


def bfs(graph, n, start):
    dist = [-1] * n
    dist[start] = 0
    next_visit = deque([start])
    while next_visit:
        cur = next_visit.popleft()
        for i, w in graph[cur]:
            if dist[i] > -1:
                continue
            dist[i] = dist[cur] + w
            next_visit.append(i)

    return dist


def main():
    input = stdin.readline
    n = int(input())
    g = [[] for _ in [0] * n]
    for _ in [0] * (n - 1):
        u, v, w = map(int, input().split())
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))
    res = [i % 2 for i in bfs(g, n, 0)]
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
