from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    s = [int(input()) for _ in [0] * n]
    if 0 in s:
        print(n)
    else:
        q = deque()
        res = 0
        tmp = 1
        for r in s:
            q.append(r)
            tmp *= r
            while q and k < tmp:
                tmp //= q.popleft()
            if res < len(q):
                res = len(q)
        print(res)


if __name__ == "__main__":
    main()
