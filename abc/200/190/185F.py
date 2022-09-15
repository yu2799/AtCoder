from sys import stdin


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, left, right):
        res = self.ide_ele

        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                res = self.segfunc(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.segfunc(res, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return res


def segfunc(x, y):
    return x ^ y


def main():
    input = stdin.readline
    _, q = map(int, input().split())
    a = list(map(int, input().split()))
    seg = SegTree(a, segfunc, 0)
    res = []
    for _ in [0] * q:
        t, x, y = map(int, input().split())
        if t == 1:
            seg.update(x - 1, seg.query(x - 1, x) ^ y)
        else:
            res.append(seg.query(x - 1, y))
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
