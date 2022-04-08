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
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return True

    def size(self, x):
        return -self.parents[self.find(x)]


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    abc = [tuple(map(int, input().split())) for _ in [0] * m]
    res = 0
    abc.sort(key=lambda x: x[2])
    uf = UnionFind(n + 1)
    for a, b, c in abc:
        if not uf.union(a, b) and c > 0:
            res += c
    print(res)


if __name__ == "__main__":
    main()
