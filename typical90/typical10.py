from itertools import accumulate
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = []
    b = []
    res = []
    for _ in range(n):
        c, p = map(int, input().split())
        if c == 1:
            a.append(p)
            b.append(0)
        else:
            a.append(0)
            b.append(p)
    a_accm = list(accumulate(a, initial=0))
    b_accm = list(accumulate(b, initial=0))
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        res.append((a_accm[r] - a_accm[l - 1], b_accm[r] - b_accm[l - 1]))
    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
