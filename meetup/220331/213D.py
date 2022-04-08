from sys import stdin

from collections import deque


def dfs(graph, n):
    visited = [False] * (n + 1)
    res = []
    next_visit = deque()
    next_visit.append(1)
    while next_visit:
        cur = next_visit.pop()
        res.append(cur)
        if visited[cur]:
            continue
        visited[cur] = True
        graph[cur].sort(reverse=True)
        for i in graph[cur]:
            if not visited[i]:
                next_visit.append(cur)
                next_visit.append(i)

    return res


def main():
    input = stdin.readline
    n = int(input())
    g = [[] for _ in [0] * (n + 1)]
    for _ in [0] * (n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    print(*dfs(g, n))


if __name__ == "__main__":
    main()
