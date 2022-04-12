from sys import stdin
from collections import deque


def bfs(graph, n, k):
    dist = [-1] * n
    dist[k] = 0
    next_visit = deque([k])
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if dist[i[0]] > -1:
                continue
            dist[i[0]] = dist[cur] + i[1]
            next_visit.append(i[0])

    return dist


def main():
    input = stdin.readline
    n = int(input())
    g = [[] for _ in [0] * n]
    res = []
    for _ in [0] * (n - 1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append((b, c))
        g[b].append((a, c))
    q, k = map(int, input().split())
    dist = bfs(g, n, k-1)
    for _ in [0] * q:
        x, y = [int(i) - 1 for i in input().split()]
        res.append(dist[x] + dist[y])
    print(*res, sep="\n")


if __name__ == '__main__':
    main()
