from sys import stdin


def main():
    input = stdin.readline
    h, n = map(int, input().split())
    INF = 10**8
    dp = [[INF] * (h + 1) for _ in [0] * (n + 1)]
    dp[0][h] = 0
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(h, -1, -1):
            tmp = max(0, j - a)
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
            dp[i][tmp] = min(dp[i][j] + b, dp[i][tmp])
    print(dp[n][0])


if __name__ == "__main__":
    main()
