from collections import deque
from sys import stdin


def bfs(graph, start, a, visited):
    next_visit = deque([start])
    res = -2 * 10**9
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if res < a[i][0]:
                res = a[i][0]
            if i in visited:
                continue
            visited.add(i)
            next_visit.append(i)
    return res


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = [(i, idx) for idx, i in enumerate(map(int, input().split()))]
    tmp = sorted(a)
    g = [[] for _ in [0] * n]
    for _ in [0] * m:
        x, y = map(lambda x: int(x) - 1, input().split())
        g[x].append(y)
    res = -2 * 10**9
    visited = set()
    for buy, start in tmp:
        if start in visited:
            continue
        visited.add(start)
        tmp = bfs(g, start, a, visited) - buy
        if res < tmp:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
