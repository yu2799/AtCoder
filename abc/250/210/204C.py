from sys import stdin
from collections import deque


def bfs(graph, n):
    res = n
    for i in range(n):
        dist = [-1] * n
        dist[i] = 0
        next_visit = deque([i])
        while next_visit:
            cur = next_visit.popleft()
            for i in graph[cur]:
                if dist[i] > -1:
                    continue
                dist[i] = dist[cur] + 1
                next_visit.append(i)
                res = res + 1
    return res


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in [0] * n]
    for _ in [0] * m:
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)

    print(bfs(g, n))


if __name__ == "__main__":
    main()
