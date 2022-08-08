from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    g = [set() for _ in [0] * n]
    for _ in [0] * m:
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].add(v)
        g[v].add(u)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if i in g[j] and j in g[k] and k in g[i]:
                    res = res + 1
    print(res)


if __name__ == "__main__":
    main()
