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
    cnt = 0
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
            cnt += 1
    print(m - cnt)


if __name__ == "__main__":
    main()
