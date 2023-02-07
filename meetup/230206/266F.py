from collections import deque
from sys import stdin


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]


def main():
    input = stdin.readline
    n = int(input())
    uv = set()
    g = [[] for _ in range(n)]
    uv = [] * n
    deg = [0] * n
    for _ in range(n):
        u, v = map(lambda x: int(x) - 1, input().split())
        uv.append((u, v))
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    uf = UnionFind(n)
    q = deque()
    for i in range(n):
        if deg[i] == 1:
            q.append(i)
    while q:
        cur = q.pop()
        for i in g[cur]:
            if deg[i] > 1:
                deg[i] -= 1
                uf.union(i, cur)
                if deg[i] == 1:
                    q.append(i)

    res = []
    q = int(input())
    for _ in range(q):
        x, y = map(lambda x: int(x) - 1, input().split())
        res.append("Yes" if uf.find(x) == uf.find(y) else "No")
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
