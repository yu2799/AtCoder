from sys import stdin
from heapq import heappop, heappush
from collections import defaultdict


class HeapDict:
    def __init__(self):
        self.h = []
        self.d = dict()

    def insert(self, x):
        heappush(self.h, x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    def erase(self, x):
        if x not in self.d or self.d[x] == 0:
            print(x, "is not in HeapDict")
            exit()
        else:
            self.d[x] -= 1

        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heappop(self.h)
            else:
                break

    def is_exist(self, x):
        if x in self.d and self.d[x] != 0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]


def main():
    input = stdin.readline
    q = int(input())
    res = []
    hq = HeapDict()
    lq = HeapDict()
    d = defaultdict(int)
    for _ in [0] * q:
        (*query,) = map(int, input().split())
        if query[0] == 1:
            hq.insert(-query[1])
            lq.insert(query[1])
            d[query[1]] += 1
        elif query[0] == 2:
            for _ in [0] * min(query[2], d[query[1]]):
                hq.erase(-query[1])
                lq.erase(query[1])
                d[query[1]] -= 1
        else:
            res.append(-hq.get_min() - lq.get_min())
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
