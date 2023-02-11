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
    return [0 if i % 2 == 0 else 1 for i in dist]


def main():
    input = stdin.readline
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append((v, w))
        g[v].append((u, w))
    print(*bfs(g, n, 0), sep="\n")


if __name__ == "__main__":
    main()
