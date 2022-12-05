from collections import defaultdict, deque
from sys import stdin


def dfs(graph):
    res = 1
    visited = set()
    next_visit = deque([1])
    while next_visit:
        cur = next_visit.pop()
        if cur not in visited:
            # 行きがけ
            next_visit.append(cur)
            visited.add(cur)
            for i in graph[cur]:
                next_visit.append(i)
                if res < i:
                    res = i
    return res


def main():
    input = stdin.readline
    n = int(input())
    g = defaultdict(list)
    for _ in [0] * n:
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    print(dfs(g))


if __name__ == "__main__":
    main()
