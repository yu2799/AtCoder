from collections import deque
from sys import stdin


def bfs(graph, n, start):
    dist = [-1] * n
    dist[start] = 0
    prev = [-2] * n
    prev[start] = -1
    next_visit = deque([start])
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if dist[i] > -1:
                continue
            dist[i] = dist[cur] + 1
            prev[i] = cur
            next_visit.append(i)
    return prev


def main():
    input = stdin.readline
    n, x, y = map(int, input().split())
    g = [[] for _ in [0] * n]
    for _ in [0] * (n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)

    res = bfs(g, n, x - 1)
    cur = y - 1
    tmp = []
    while cur != -1:
        tmp.append(cur + 1)
        cur = res[cur]
    tmp.reverse()
    print(*tmp)


if __name__ == "__main__":
    main()
