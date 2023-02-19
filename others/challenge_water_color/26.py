from collections import deque
from sys import stdin


def dfs(graph, d):
    visited = set()
    next_visit = deque([0])
    while next_visit:
        cur = next_visit.pop()
        if cur in visited:
            continue
        visited.add(cur)
        for i in graph[cur]:
            if i in visited:
                continue
            next_visit.append(i)
            d[i] += d[cur]

    return d


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    d = [0] * n
    for _ in range(q):
        p, x = map(int, input().split())
        d[p - 1] += x
    print(*dfs(graph, d))


if __name__ == "__main__":
    main()
