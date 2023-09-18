from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    q = int(input())
    dq = deque()
    res = []
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            dq.appendleft(x)
        elif t == 2:
            dq.append(x)
        else:
            res.append(dq[x - 1])
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
