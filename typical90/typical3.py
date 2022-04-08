from sys import stdin
from collections import deque


def bfs(graph, n):
    dist = [-1] * n
    dist[0] = 0
    next_visit = deque([0])
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if dist[i] != -1:
                continue
            dist[i] = dist[cur] + 1
            next_visit.append(i)

    point = dist.index(max(dist))
    dist = [-1] * n
    dist[point] = 0
    next_visit = deque([point])
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if dist[i] != -1:
                continue
            dist[i] = dist[cur] + 1
            next_visit.append(i)

    return max(dist) + 1


def main():
    input = stdin.readline
    n = int(input())
    g = [[] for _ in [0] * n]
    for _ in [0] * (n-1):
        a, b = [int(i) - 1 for i in input().split()]
        g[a].append(b)
        g[b].append(a)
    print(bfs(g, n))


if __name__ == '__main__':
    main()
