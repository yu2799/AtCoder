from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    MOD = 998244353
    dp = [[0] * 11 for _ in [0] * (n + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, n + 1):
        for j in range(1, 10):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
            dp[i][j] %= MOD
    print(sum(dp[n]) % MOD)


if __name__ == "__main__":
    main()
