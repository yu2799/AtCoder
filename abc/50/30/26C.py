from sys import stdin
from collections import deque


def dfs(graph, n):
    res = [0] * n
    visited = set()
    next_visit = deque([(0, -1)])
    while next_visit:
        cur, parent = next_visit.pop()
        if cur != 0 and len(graph[cur]) == 1:
            res[cur] = 1
        elif cur in visited:
            left = -1
            right = 10**18
            for i in graph[cur]:
                if i != parent:
                    left = max(left, res[i])
                    right = min(right, res[i])
            res[cur] = left + right + 1
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
    g = [[] for _ in [0] * n]
    for i in range(1, n):
        b = int(input()) - 1
        g[i].append(b)
        g[b].append(i)
    print(dfs(g, n)[0])


if __name__ == "__main__":
    main()
