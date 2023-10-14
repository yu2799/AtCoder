from collections import deque
from sys import stdin


def bfs(graph, n, start=0):
    dist = [-1] * n
    dist[start] = 0
    next_visit = deque([start])
    even = [1]
    odd = []
    while next_visit:
        cur = next_visit.popleft()
        for i in graph[cur]:
            if dist[i] > -1:
                continue
            dist[i] = dist[cur] + 1
            next_visit.append(i)
            if dist[i] % 2:
                odd.append(i + 1)
            else:
                even.append(i + 1)

    return odd[: n // 2] if len(even) < len(odd) else even[: n // 2]


def main():
    input = stdin.readline
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(*bfs(graph, n))


if __name__ == "__main__":
    main()
