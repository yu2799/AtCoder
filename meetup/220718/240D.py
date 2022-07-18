from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    q = deque()
    res = []
    cnt = 0
    for i in a:
        if not q or q[-1][0] != i:
            q.append((i, 1))
            cnt = cnt + 1
        else:
            rm = q.pop()
            q.append((rm[0], rm[1] + 1))
            if rm[0] == rm[1] + 1:
                q.pop()
                cnt = cnt - rm[0]
            cnt = cnt + 1
        res.append(cnt)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
