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

        # 共通祖先を持つ = 閉路を持つ
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
    g = [[] for _ in [0] * n]
    uf = UnionFind(n)
    cnt = [0] * n
    for _ in [0] * m:
        a, b = [int(i) - 1 for i in input().split()]
        g[a].append(b)
        g[b].append(a)
        cnt[a] += 1
        cnt[b] += 1
        if not uf.union(a, b) or cnt[a] > 2 or cnt[b] > 2:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
