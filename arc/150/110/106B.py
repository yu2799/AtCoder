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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    uf = UnionFind(n)
    cnt_a = [0] * n
    cnt_b = [0] * n
    for _ in [0] * m:
        c, d = [int(i) - 1 for i in input().split()]
        uf.union(c, d)
    for i, j in enumerate(uf.parents):
        if j > -1:
            j = uf.find(j)
            cnt_a[j] += a[i]
            cnt_b[j] += b[i]
        else:
            cnt_a[i] += a[i]
            cnt_b[i] += b[i]
    for i, j in zip(cnt_a, cnt_b):
        if i != j:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    main()
