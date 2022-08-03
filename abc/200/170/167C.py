from sys import stdin


def main():
    input = stdin.readline
    n, m, x = map(int, input().split())
    c = [0] * n
    a = [None] * n
    INF = float("inf")
    res = INF
    for i in range(n):
        c[i], *a[i] = map(int, input().split())

    for i in range(1, 2**n):
        d = [0] * m
        tmp = 0
        for idx, j in enumerate(str(bin(i))[2:].zfill(n)):
            if j == "1":
                tmp = tmp + c[idx]
                for k in range(m):
                    d[k] = d[k] + a[idx][k]
        for i in d:
            if i < x:
                break
        else:
            if tmp < res:
                res = tmp
    print(res if res != INF else -1)


if __name__ == "__main__":
    main()
