from sys import stdin
from collections import deque


def bfs(graph, n):
    dist = [-1] * n
    dist[0] = 0
    cnt = [0] * n
    cnt[0] = 1
    MOD = 10 ** 9 + 7
    next_visit = deque([0])
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if dist[i] == -1:
                dist[i] = dist[cur] + 1
                next_visit.append(i)
                cnt[i] = cnt[cur]
            elif dist[i] == dist[cur] + 1:
                cnt[i] += cnt[cur]
                cnt[i] %= MOD

    return cnt[-1]


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in [0] * n]
    for _ in [0] * m:
        a, b = [int(i) - 1 for i in input().split()]
        g[a].append(b)
        g[b].append(a)
    print(bfs(g, n))


if __name__ == "__main__":
    main()
