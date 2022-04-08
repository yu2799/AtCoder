from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    dp = [[0] * n for _ in [0] * n]
    dp[0] = a
    for i in range(1, n):
        for j in range(n):
            dp[i][j] += dp[i - 1][j]
            dp[i][j] %= 100
            if j - 1 > -1:
                dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] %= 100
            if j + 1 < n:
                dp[i][j] += dp[i - 1][j + 1]
                dp[i][j] %= 100
    print(dp[n - 1][-1])


if __name__ == "__main__":
    main()
