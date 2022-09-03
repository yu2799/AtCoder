from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[-(10**18)] * (m + 1) for _ in [0] * (n + 1)]
    res = -(10**18)
    for i in range(n):
        dp[i][0] = 0
        for j in range(min(i + 1, m)):
            dp[i + 1][j + 1] = max(dp[i][j] + a[i] * (j + 1), dp[i][j + 1])
    for i in range(m + 1, n + 1):
        res = max(res, dp[i][m])
    print(res)


if __name__ == "__main__":
    main()
