from sys import stdin
from collections import deque


def bfs(a, n):
    dist = [-1] * 10**6
    dist[1] = 0
    next_visit = deque([1])
    while next_visit:
        cur = next_visit.popleft()
        i = cur * a
        if i <= n and dist[i] == -1:
            dist[i] = dist[cur] + 1
            next_visit.append(i)

        if len(str(cur)) >= 2 and str(cur)[-1] != "0":
            i = int(str(cur)[-1] + str(cur)[:-1])
            if dist[i] == -1:
                dist[i] = dist[cur] + 1
                next_visit.append(i)
    return dist


def main():
    input = stdin.readline
    a, n = map(int, input().split())
    print(bfs(a, 10**6)[n])


if __name__ == "__main__":
    main()
