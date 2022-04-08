from sys import stdin
from collections import deque, defaultdict


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    a = [i for i in map(int, input().split())]
    q = deque()
    cnt = 0
    d = defaultdict(int)
    res = 0
    for r in a:
        q.append(r)
        if d[r] == 0:
            cnt += 1
        d[r] += 1
        while q and k < cnt:
            rm = q.popleft()
            d[rm] -= 1
            while q and rm == q[0]:
                q.popleft()
                d[rm] -= 1
            if d[rm] == 0:
                cnt -= 1
        if res < len(q):
            res = len(q)
    print(res)


if __name__ == '__main__':
    main()
