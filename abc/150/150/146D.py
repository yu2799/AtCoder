from collections import deque
from sys import stdin


def bfs(graph, n):
    res = [0] * n
    next_visit = deque([0])
    while next_visit:
        cur = next_visit.popleft()
        color = 0
        for i in graph[cur]:
            color += 1 + (color + 1 == res[cur])
            res[i] = color
            next_visit.append(i)
    return res


def main():
    input = stdin.readline
    n = int(input())
    g = [[] for _ in [0] * n]
    e = []
    for _ in [0] * (n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)
        e.append(b)
    res = bfs(g, n)
    print(max(res))
    print(*[res[i] for i in e], sep="\n")


if __name__ == "__main__":
    main()
