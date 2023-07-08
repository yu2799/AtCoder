from collections import defaultdict, deque
from sys import stdin


def dfs(graph):
    res = 0
    visited = set()
    next_visit = deque([1])
    while next_visit:
        cur = next_visit.pop()
        if res < cur:
            res = cur
        if cur not in visited:
            next_visit.append(cur)
            visited.add(cur)
            for i in graph[cur]:
                next_visit.append(i)

    return res


def main():
    input = stdin.readline
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(dfs(graph))


if __name__ == "__main__":
    main()
