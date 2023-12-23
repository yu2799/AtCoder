from collections import deque
from sys import stdin


def bfs(graph, n):
    dist = [-1] * n

    for i in range(n):
        if dist[i] > -1:
            continue
        dist[i] = 0
        next_visit = deque([i])
        while next_visit:
            cur = next_visit.popleft()
            for i in graph[cur]:
                if dist[i] > -1:
                    if dist[i] == dist[cur]:
                        return False
                else:
                    dist[i] = 1 - dist[cur]
                    next_visit.append(i)
    return True


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))
    b = list(map(lambda x: int(x) - 1, input().split()))
    graph = [[] for _ in range(n)]
    for i, j in zip(a, b):
        graph[i].append(j)
        graph[j].append(i)
    print("Yes" if bfs(graph, n) else "No")


if __name__ == "__main__":
    main()
