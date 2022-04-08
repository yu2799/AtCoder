from sys import stdin
from collections import deque


def bfs(graph, n):
    dist = [-1] * n
    dist[0] = 0
    next_visit = deque([0])
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if dist[i] > -1:
                continue
            dist[i] = dist[cur] + 1
            next_visit.append(i)

    return dist


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in [0] * n]
    for _ in [0] * m:
        a, b = [int(i) - 1 for i in input().split()]
        g[a].append(b)
        g[b].append(a)
    dist = bfs(g, n)
    if dist[n - 1] == 2:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
