from sys import stdin
from collections import deque


def dfs(graph, n, x):
    res = [[] for _ in [0] * n]
    visited = set()
    next_visit = deque([(0, -1)])
    while next_visit:
        cur, parent = next_visit.pop()
        if cur in visited:
            tmp = [x[cur]]
            for i in graph[cur]:
                if i != parent:
                    tmp += res[i]
            res[cur] = sorted(tmp, reverse=True)[:20]
        else:
            next_visit.append((cur, parent))
            visited.add(cur)
            for i in graph[cur]:
                if i != parent:
                    next_visit.append((i, cur))
    return res


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    g = [[] for _ in [0] * n]
    for _ in [0] * (n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)
        g[b].append(a)
    tmp = dfs(g, n, x)
    res = []
    for _ in [0] * q:
        v, k = map(lambda x: int(x) - 1, input().split())
        res.append(tmp[v][k])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
