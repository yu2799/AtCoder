from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    graph = [set() for _ in range(n)]
    deg = [0] * n
    for _ in range(m):
        x, y = map(lambda x: int(x) - 1, input().split())
        if y not in graph[x]:
            graph[x].add(y)
            deg[y] += 1
    q = deque()
    for i in range(n):
        if deg[i] == 0:
            q.append(i)

    cnt = 1
    res = [0] * n
    while q:
        if len(q) != 1:
            print("No")
            return
        cur = q.pop()
        for i in graph[cur]:
            deg[i] -= 1
            if deg[i] == 0:
                q.append(i)
        res[cur] = cnt
        cnt += 1
    print("Yes")
    print(*res)


if __name__ == "__main__":
    main()
