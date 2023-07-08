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

    return dist


def main():
    input = stdin.readline
    n1, n2, m = map(int, input().split())
    graph = [[] for _ in range(n1 + n2)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    d1 = bfs(graph, n1 + n2, 0)
    d2 = bfs(graph, n1 + n2, n1 + n2 - 1)
    print(max(d1) + max(d2) + 1)


if __name__ == "__main__":
    main()
