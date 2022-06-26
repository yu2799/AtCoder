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
    return -1 not in dist


def check(g, n):
    for i in range(n):
        if bfs(g, n, i):
            return True
    return False


def main():
    input = stdin.readline
    n = int(input())
    far = [[0] * n for _ in [0] * n]
    xyp = [tuple(map(int, input().split())) for _ in [0] * n]
    for i in range(n - 1):
        for j in range(i + 1, n):
            tmp = abs(xyp[i][0] - xyp[j][0]) + abs(xyp[i][1] - xyp[j][1])
            far[i][j] = tmp
            far[j][i] = tmp
    ng = 0
    ok = 4 * 10**9 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        g = [[] for _ in [0] * n]

        for i in range(n - 1):
            for j in range(i + 1, n):
                if xyp[i][2] * mid >= far[i][j]:
                    g[i].append(j)
                if xyp[j][2] * mid >= far[j][i]:
                    g[j].append(i)
        if check(g, n):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()
