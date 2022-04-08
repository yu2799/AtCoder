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

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    if n != m:
        print(0)
        return

    uf = UnionFind(n)
    deg = [0] * n
    cnt = [0] * m
    MOD = 998244353
    for _ in [0] * m:
        u, v = [int(i) - 1 for i in input().split()]
        uf.union(u, v)
        deg[u] += 1
    for i in range(n):
        x = uf.root(i)
        cnt[x] += deg[i]
    res = 0
    for i in range(n):
        if uf.parents[i] < 0:
            node = -uf.parents[i]
            if node == cnt[i]:
                res += 1
            else:
                print(0)
                return
    else:
        print(pow(2, res, MOD))


if __name__ == "__main__":
    main()
