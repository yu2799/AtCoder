from collections import deque
from sys import stdin


def dfs(graph, n):
    res = []
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        next_visit = deque([i])
        while next_visit:
            cur = next_visit.pop()
            if cur not in visited:
                # 行きがけ
                next_visit.append(cur)
                visited.add(cur)
                if len(graph[cur]) > 0:
                    for i in graph[cur]:
                        next_visit.append(i)
                else:
                    res.append(cur)
    return res[0] + 1 if len(set(res)) == 1 else -1


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[b].append(a)
    if m == 0:
        print(-1)
    else:
        print(dfs(graph, n))


if __name__ == "__main__":
    main()
