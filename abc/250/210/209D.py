from collections import deque
from sys import stdin


def bfs(graph, n, start):
    dist = [-1] * n
    dist[start] = 0
    next_visit = deque([start])
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if dist[i] > -1:
                continue
            dist[i] = dist[cur] + 1
            next_visit.append(i)

    return dist


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    g = [[] for _ in [0] * n]
    for _ in [0] * (n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)
        g[b].append(a)
    res = []
    dist = bfs(g, n, 0)
    for _ in [0] * q:
        c, d = map(lambda x: int(x) - 1, input().split())
        if (dist[c] - dist[d]) % 2 == 0:
            res.append("Town")
        else:
            res.append("Road")
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
