from sys import stdin
from collections import deque


def dfs(graph, n):
    res = [None] * n
    visited = set()
    next_visit = deque([(0, -1)])
    cnt = 1
    while next_visit:
        cur, parent = next_visit.pop()
        if cur != 0 and len(graph[cur]) == 1:
            res[cur] = (cnt, cnt)
            cnt = cnt + 1
        elif cur in visited:
            left = 2 * 10**5
            right = -1
            for i in graph[cur]:
                if i != parent:
                    left = min(left, res[i][0])
                    right = max(right, res[i][1])
            res[cur] = (left, right)
        else:
            next_visit.append((cur, parent))
            visited.add(cur)
            for i in graph[cur]:
                if i != parent:
                    next_visit.append((i, cur))
    return res


def main():
    input = stdin.readline
    n = int(input())
    g = [[] for _ in [0] * (n + 1)]
    for _ in [0] * (n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)
    res = dfs(g, n)
    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
