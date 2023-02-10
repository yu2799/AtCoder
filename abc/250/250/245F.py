from collections import deque
from sys import stdin


def dfs(graph, n, deg):
    visited = set()
    next_visit = deque()
    for i in range(n):
        if deg[i] == 0:
            next_visit.append(i)
    while next_visit:
        cur = next_visit.pop()
        visited.add(cur)
        for i in graph[cur]:
            if i in visited:
                continue
            deg[i] -= 1
            if deg[i] == 0:
                next_visit.append(i)

    return len([1 for i in deg if i > 0])


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[v].append(u)
        deg[u] += 1

    print(dfs(g, n, deg))


if __name__ == "__main__":
    main()
