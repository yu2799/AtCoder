from sys import stdin
from collections import deque


def bfs(a, n):
    dist = [-1] * 10**6
    dist[n] = 0
    next_visit = deque([n])
    while next_visit:
        cur = next_visit.popleft()
        if cur % a == 0:
            tmp = cur // a
            if dist[tmp] == -1:
                dist[tmp] = dist[cur] + 1
                next_visit.append(tmp)
        if len(str(cur)) >= 2 and str(cur)[1] != "0":
            tmp = int(str(cur)[1:] + str(cur)[0])
            if dist[tmp] == -1:
                dist[tmp] = dist[cur] + 1
                next_visit.append(tmp)

    return dist


def main():
    input = stdin.readline
    a, n = map(int, input().split())
    print(bfs(a, n)[1])


if __name__ == "__main__":
    main()
