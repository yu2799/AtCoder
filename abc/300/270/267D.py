from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    INF = float("inf")
    dp = [[-INF] * (m + 1) for _ in range(n + 1)]
    res = -INF
    for i in range(n):
        dp[i][0] = 0
        for j in range(m):
            if i < j:
                break
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + a[i] * (j + 1))
    for i in range(m + 1, n + 1):
        res = max(res, dp[i][m])
    print(res)


if __name__ == "__main__":
    main()
