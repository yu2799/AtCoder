from collections import defaultdict, deque
from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    res = 0
    d = defaultdict(int)
    q = deque()
    for i in range(k):
        if d[c[i]] == 0:
            res += 1
        q.append(c[i])
        d[c[i]] += 1

    tmp = res
    for i in range(k, n):
        rm = q.popleft()
        d[rm] -= 1
        if d[rm] == 0:
            tmp -= 1
        if d[c[i]] == 0:
            tmp += 1
        q.append(c[i])
        d[c[i]] += 1
        if res < tmp:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
