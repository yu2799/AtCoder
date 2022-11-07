from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in [0] * n]
    for _ in [0] * m:
        a, b = map(lambda x: int(x) - 1, input().split())
        g[a].append(b)
        g[b].append(a)
    res = []
    for i in g:
        tmp = [len(i)]
        i.sort()
        for j in i:
            tmp.append(j + 1)
        res.append(tmp)
    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
