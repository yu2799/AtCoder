from sys import stdin
from collections import deque


def dfs(graph, n, val):
    visited = [False] * (n + 1)
    next_visit = deque()
    next_visit.append(1)
    while next_visit:
        cur = next_visit.pop()
        if visited[cur]:
            continue
        visited[cur] = True
        for i in graph[cur]:
            if not visited[i]:
                next_visit.append(i)
                val[i] += val[cur]

    return val[1:]


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    g = [[] for _ in [0] * (n + 1)]
    val = [0] * (n + 1)
    for _ in [0] * (n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    for _ in [0] * q:
        p, x = map(int, input().split())
        val[p] += x
    print(*dfs(g, n, val))


if __name__ == "__main__":
    main()
