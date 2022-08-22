from sys import stdin


def main():
    input = stdin.readline
    n, w = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in [0] * n]
    MAX_VALUE = sum([i[1] for i in wv]) + 1
    INF = 10**15
    dp = [[INF] * MAX_VALUE for _ in [0] * (n + 1)]
    dp[0][0] = 0
    for i in range(n):
        weight, value = wv[i]
        for j in range(MAX_VALUE):
            if j + value < MAX_VALUE:
                dp[i + 1][j + value] = min(
                    dp[i][j] + weight, dp[i + 1][j + value]
                )
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    res = 0
    for i in range(MAX_VALUE):
        if dp[n][i] <= w:
            res = i
    print(res)


if __name__ == "__main__":
    main()
