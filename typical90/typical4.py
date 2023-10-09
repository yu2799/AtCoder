from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    res = [[0] * m for _ in range(n)]
    col_sum = [0] * m
    row_sum = [0] * n
    for i in range(n):
        for j in range(m):
            row_sum[i] += a[i][j]
            col_sum[j] += a[i][j]

    for i in range(n):
        for j in range(m):
            res[i][j] = row_sum[i] + col_sum[j] - a[i][j]

    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
