from itertools import permutations, product
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    s = [input()[:-1] for _ in [0] * n]
    t = set(input()[:-1] for _ in [0] * m)
    limit = 16 - sum([len(i) for i in s]) - (n - 1)
    tmp = [
        i
        for i in product(list(range(limit + 1)), repeat=(n - 1))
        if sum(i) <= limit
    ]
    for i in permutations(s):
        for j in tmp:
            buf = i[0]
            for idx, k in enumerate(j):
                buf = buf + "_" * (int(k) + 1) + i[idx + 1]
            if buf not in t and 3 <= len(buf) <= 16:
                print(buf)
                return
    print(-1)


if __name__ == "__main__":
    main()
