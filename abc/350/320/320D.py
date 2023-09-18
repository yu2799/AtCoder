from collections import deque
from sys import stdin


def bfs(graph, n):
    res = [None] * n
    res[0] = (0, 0)
    dist = [-1] * n
    dist[0] = 0
    next_visit = deque([0])
    while next_visit:
        cur = next_visit.popleft()
        for pos, dx, dy in graph[cur]:
            if dist[pos] > -1:
                continue
            dist[pos] = dist[cur] + 1
            next_visit.append(pos)
            x = dx + res[cur][0]
            y = dy + res[cur][1]
            res[pos] = (x, y)
    return res


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    graph = [set() for _ in range(n)]
    for _ in range(m):
        a, b, x, y = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].add((b, x, y))
        graph[b].add((a, -x, -y))
    res = bfs(graph, n)
    for i in res:
        if i:
            print(*i)
        else:
            print("undecidable")


if __name__ == "__main__":
    main()
