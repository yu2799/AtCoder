from collections import deque
from sys import stdin


def bfs(graph, n, start, end, a):
    dist = [-1] * n
    cost = [0] * n
    dist[start] = 0
    cost[start] = a[start]
    next_visit = deque([start])
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if dist[i] == -1:
                dist[i] = dist[cur] + 1
                cost[i] = cost[cur] + a[i]
                next_visit.append(i)
            elif dist[i] == dist[cur] + 1:
                if cost[i] < cost[cur] + a[i]:
                    cost[i] = cost[cur] + a[i]
    if dist[end] != -1:
        return dist[end], cost[end]
    else:
        return False


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    INF = 10**18
    cost = [[INF] * n for _ in [0] * n]
    tmp = [[0] * n for _ in [0] * n]
    for i in range(n):
        s = input()[:-1]
        for j in range(n):
            if s[j] == "Y":
                cost[i][j] = 1
                tmp[i][j] = a[j]
    for i in range(n):
        cost[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    if cost[i][k] + cost[k][j] < cost[i][j]:
                        cost[i][j] = cost[i][k] + cost[k][j]
                        tmp[i][j] = tmp[i][k] + tmp[k][j]
                    elif cost[i][k] + cost[k][j] == cost[i][j]:
                        tmp[i][j] = max(tmp[i][j], tmp[i][k] + tmp[k][j])
    q = int(input())
    for _ in [0] * q:
        u, v = map(lambda x: int(x) - 1, input().split())
        if cost[u][v] < INF:
            print(cost[u][v], tmp[u][v] + a[u])
        else:
            print("Impossible")


if __name__ == "__main__":
    main()
