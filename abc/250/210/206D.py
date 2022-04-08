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
    uf = UnionFind(2 * 10 ** 5 + 1)
    a = [int(i) - 1 for i in input().split()]
    res = 0
    for i in range(n // 2):
        uf.union(a[i], a[n - 1 - i])
    for i in uf.parents:
        if i < -1:
            res += -i - 1
    print(res)


if __name__ == "__main__":
    main()
