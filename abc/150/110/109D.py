from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in [0] * h]
    n = 0
    res = []
    for i in range(h):
        for j in range(w - 1):
            if a[i][j] % 2:
                a[i][j + 1] += 1
                n += 1
                res.append([i + 1, j + 1, i + 1, j + 2])
    for i in range(h - 1):
        if a[i][w - 1] % 2:
            a[i + 1][w - 1] += 1
            n += 1
            res.append([i + 1, w, i + 2, w])
    print(n)
    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
