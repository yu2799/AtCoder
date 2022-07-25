from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0] * 10 for _ in [0] * n]
    dp[0][a[0]] = 1
    for i in range(n - 1):
        for j in range(10):
            dp[i][j] %= MOD
            dp[i + 1][(j + a[i + 1]) % 10] += dp[i][j]
            dp[i + 1][(j * a[i + 1]) % 10] += dp[i][j]
    for i in range(10):
        print(dp[-1][i] % MOD)


if __name__ == "__main__":
    main()
