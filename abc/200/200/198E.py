from sys import stdin
from collections import deque, defaultdict


def dfs(graph, n, c):
    res = []
    d = defaultdict(int)
    visited = set()
    next_visit = deque([(0, -1)])
    while next_visit:
        cur, parent = next_visit.pop()
        if cur not in visited:
            next_visit.append((cur, parent))
            visited.add(cur)
            if d[c[cur]] == 0:
                res.append(cur + 1)
            d[c[cur]] = d[c[cur]] + 1
            for i in graph[cur]:
                if i != parent:
                    next_visit.append((i, cur))
        else:
            d[c[cur]] = d[c[cur]] - 1
    res.sort()
    return res


def main():
    input = stdin.readline
    n = int(input())
    c = list(map(int, input().split()))
    g = [[] for _ in [0] * n]
    for _ in [0] * (n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)
        g[b].append(a)
    print(*dfs(g, n, c), sep="\n")


if __name__ == "__main__":
    main()
