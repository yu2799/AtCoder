from sys import stdin
from collections import deque


def main():
    input = stdin.readline
    n, q = map(int, input().split())
    g = [[] for _ in [0] * (n + 1)]
    visited = [False] * (n + 1)
    visited[0] = True
    d = deque([0])
    for _ in [0] * q:
        l, r = map(int, input().split())
        g[l - 1].append(r)
        g[r].append(l - 1)
    while d:
        rm = d.popleft()
        if rm == n:
            print("Yes")
            exit()
        for i in g[rm]:
            if not visited[i]:
                d.append(i)
                visited[i] = True
    print("No")


if __name__ == "__main__":
    main()
