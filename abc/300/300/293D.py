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
    n, m = map(int, input().split())
    uf = UnionFind(n)
    x = 0
    y = 0
    for _ in range(m):
        a, b, c, d = input().split()
        a = int(a) - 1
        c = int(c) - 1
        if uf.find(a) == uf.find(c):
            x += 1
        uf.union(a, c)
    for i in uf.parents:
        if i < 0:
            y += 1
    print(x, y - x)


if __name__ == "__main__":
    main()
