from collections import deque
from sys import stdin


def bfs(graph, n, start):
    dist = [-1] * n
    dist[start] = 0
    next_visit = deque([start])
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if dist[i] > -1:
                continue
            dist[i] = dist[cur] + 1
            next_visit.append(i)

    s = dist.index(max(dist))

    dist = [-1] * n
    dist[s] = 0
    next_visit = deque([s])
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if dist[i] > -1:
                continue
            dist[i] = dist[cur] + 1
            next_visit.append(i)

    return max(dist) + 1


def main():
    input = stdin.readline
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(bfs(graph, n, 0))


if __name__ == "__main__":
    main()
