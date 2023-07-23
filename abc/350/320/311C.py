from collections import deque
from sys import stdin


def topological_sort(graph, n, deg):
    q = deque()
    for i in range(n):
        if deg[i] == 0:
            q.append(i)

    res = []
    while q:
        v = q.popleft()
        res.append(v)
        for i in graph[v]:
            deg[i] -= 1
            if deg[i] == 0:
                q.append(i)
    return res


def dfs(graph, s):
    res = []
    visited = set()
    next_visit = deque([s])
    while next_visit:
        cur = next_visit.pop()
        if cur not in visited:
            next_visit.append(cur)
            visited.add(cur)
            res.append(cur + 1)
            for i in graph[cur]:
                next_visit.append(i)

    return res


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    deg = [0] * n
    for i in range(n):
        graph[i].append(a[i] - 1)
        deg[a[i] - 1] += 1
    tmp = set(topological_sort(graph, n, deg))
    for i in range(n):
        if i not in tmp:
            res = dfs(graph, i)
            print(len(res))
            print(*res)
            return


if __name__ == "__main__":
    main()
