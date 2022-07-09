from sys import stdin
from collections import deque


def dfs(graph, s, t):
    visited = set()
    next_visit = deque([s])
    while next_visit:
        cur = next_visit.pop()
        if cur == t:
            return True
        for i in graph[cur]:
            if i not in visited:
                next_visit.append(i)
                visited.add(i)

    return False


def dist(x1, x2, y1, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def onCircle(x, y, r, cx, cy):
    return (cx - x) ** 2 + (cy - y) ** 2 == r**2


def main():
    input = stdin.readline
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    xyr = [tuple(map(int, input().split())) for _ in [0] * n]
    g = [[] for _ in [0] * n]

    for i in range(n):
        x, y, r = xyr[i]
        if onCircle(x, y, r, sx, sy):
            s = i
        if onCircle(x, y, r, tx, ty):
            t = i

        for j in range(i + 1, n):
            d = dist(x, xyr[j][0], y, xyr[j][1])
            if (r - xyr[j][2]) ** 2 <= d <= (r + xyr[j][2]) ** 2:
                g[i].append(j)
                g[j].append(i)
    print("Yes" if dfs(g, s, t) else "No")


if __name__ == "__main__":
    main()
