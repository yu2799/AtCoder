from collections import deque
from sys import stdin


def bfs(graph, n, start=0):
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
    return set(idx for idx, i in enumerate(dist) if i >= 0)


def topological_sort(graph, deg, same_set):
    res = []
    next_visit = deque()

    for idx, i in enumerate(deg):
        if i == 0 and idx in same_set:
            next_visit.append(idx)

    while next_visit:
        cur = next_visit.popleft()
        if cur == 0:
            return res
        res.append(cur + 1)
        for i in graph[cur]:
            deg[i] -= 1
            if deg[i] == 0 and i in same_set:
                next_visit.append(i)


def main():
    input = stdin.readline
    n = int(input())
    graph = [[] for _ in range(n)]
    directed_graph = [[] for _ in range(n)]
    deg = [0] * n
    for i in range(n):
        _, *p = map(int, input().split())
        for j in p:
            directed_graph[j - 1].append(i)
            graph[i].append(j - 1)
            deg[i] += 1
    for i in range(n):
        directed_graph[i].sort()
    print(*topological_sort(directed_graph, deg, bfs(graph, n)))


if __name__ == "__main__":
    main()
