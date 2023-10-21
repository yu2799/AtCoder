from heapq import heappop, heappush
from sys import stdin


def dijkstra(graph, n, start):
    res = [float("inf")] * n
    res[start] = 0
    hq = []
    heappush(hq, [0, start])
    visited = set()

    while hq:
        cur_cost, cur = heappop(hq)
        if cur in visited:
            continue

        for next, cost in graph[cur]:
            tmp = cur_cost + cost
            if tmp < res[next]:
                res[next] = tmp
                heappush(hq, [tmp, next])
    return res


def main():
    input = stdin.readline
    n, a, b, c = map(int, input().split())
    car = [[] for _ in range(n)]
    train = [[] for _ in range(n)]
    for i in range(n):
        d = list(map(int, input().split()))
        for idx, j in enumerate(d):
            if i == idx:
                continue
            car[i].append([idx, j * a])
            train[i].append([idx, j * b + c])
    a = dijkstra(car, n, 0)
    b = dijkstra(train, n, n - 1)

    res = float("inf")
    for i, j in zip(a, b):
        res = min(res, i + j)
    print(res)


if __name__ == "__main__":
    main()
