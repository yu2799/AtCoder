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
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    res = [1 for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        graph[u].append(v)
        graph[v].append(u)
    tmp = [bfs(graph, n, i) for i in range(n)]

    k = int(input())
    pd = [tuple(map(int, input().split())) for _ in range(k)]
    for p, d in pd:
        p -= 1
        for i in range(n):
            if tmp[p][i] < d:
                res[i] = 0

    for p, d in pd:
        p -= 1
        for i in range(n):
            if tmp[p][i] == d and res[i] == 1:
                break
        else:
            print("No")
            return
    print("Yes")
    print(*res, sep="")


if __name__ == "__main__":
    main()
