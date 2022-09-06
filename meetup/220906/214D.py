from operator import itemgetter
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
    uvw = [tuple(map(int, input().split())) for _ in [0] * (n - 1)]
    uvw.sort(key=itemgetter(2))
    uf = UnionFind(n)
    res = 0
    for u, v, w in uvw:
        u -= 1
        v -= 1
        res += w * uf.size(u) * uf.size(v)
        uf.union(u, v)
    print(res)


if __name__ == "__main__":
    main()
