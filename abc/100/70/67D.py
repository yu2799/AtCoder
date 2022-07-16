from sys import stdin
from collections import deque


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
    n = int(input())
    g = [[] for _ in [0] * n]
    for _ in [0] * (n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)
        g[b].append(a)
    f = bfs(g, n, 0)
    s = bfs(g, n, n - 1)
    f_cnt = 0
    s_cnt = 0
    for i, j in zip(f, s):
        if i <= j:
            f_cnt = f_cnt + 1
        else:
            s_cnt = s_cnt + 1
    print("Fennec" if f_cnt > s_cnt else "Snuke")


if __name__ == "__main__":
    main()
