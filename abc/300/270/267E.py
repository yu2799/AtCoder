from sys import stdin


def solve(a, n, mid, g, c):
    stack = [i for i in range(n) if c[i] <= mid]
    visited = set(stack)
    while stack:
        rm = stack.pop()
        for i in g[rm]:
            c[i] -= a[rm]
            if i not in visited and c[i] <= mid:
                stack.append(i)
                visited.add(i)
    return len(visited) == n


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    cost = [0] * n
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        graph[u].append(v)
        graph[v].append(u)
        cost[u] += a[v]
        cost[v] += a[u]

    ng = 0
    ok = sum(a) + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(a, n, mid, graph, cost.copy()):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()
