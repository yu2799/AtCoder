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
    h, w = map(int, input().split())
    q = int(input())
    red = set()
    res = []
    uf = UnionFind(h * w)
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for _ in range(q):
        t, *query = map(lambda x: int(x) - 1, input().split())
        if t == 0:
            r, c = query
            red.add((r, c))
            for dx, dy in dir:
                next_y = r + dy
                next_x = c + dx
                if (
                    (next_y, next_x) in red
                    and 0 <= next_y < h
                    and 0 <= next_x < w
                ):
                    uf.union(r * w + c, next_y * w + next_x)
        else:
            r1, c1, r2, c2 = query
            res.append(
                "Yes"
                if (r1, c1) in red
                and (r2, c2) in red
                and uf.find(r1 * w + c1) == uf.find(r2 * w + c2)
                else "No"
            )
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
