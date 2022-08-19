from collections import deque
from sys import stdin


def bfs(graph, n):
    visited = set()
    visited.add(0)
    res = [-1] * (n - 1)
    next_visit = deque([(0)])
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if i not in visited:
                res[i - 1] = cur + 1
                next_visit.append(i)
                visited.add(i)
    return res


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in [0] * n]
    for _ in [0] * m:
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)
        g[b].append(a)
    res = bfs(g, n)
    if -1 in res:
        print("No")
    else:
        print("Yes")
        print(*res, sep="\n")


if __name__ == "__main__":
    main()
