from collections import deque
from itertools import accumulate
from sys import stdin


def main():
    input = stdin.readline
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    accm = list(accumulate(a, initial=0))

    x = 0
    tot_a = 0
    d_a = deque()
    tmp_a = []
    for i in range(n):
        d_a.append(a[i])
        tot_a += a[i]
        if p < tot_a:
            while d_a and p < tot_a:
                tot_a -= d_a.popleft()
                x += 1
        if p == tot_a:
            tmp_a.append((x, i + 1))

    y = n - 1
    tot_b = 0
    tmp_b = []
    d_b = deque()
    for i in range(n - 1, -1, -1):
        d_b.append(a[i])
        tot_b += a[i]
        if r < tot_b:
            while d_b and r < tot_b:
                tot_b -= d_b.popleft()
                y -= 1
        if r == tot_b:
            tmp_b.append((i, y))
    for i in tmp_a:
        for j in tmp_b:
            if j[0] <= i[1]:
                continue
            if accm[j[0]] - accm[i[1]] == q:
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
