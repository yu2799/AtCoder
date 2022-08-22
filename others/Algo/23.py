from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [[int(i) for i in input().split()] for _ in [0] * n]
    dp = [[0] * 3 for _ in [0] * n]
    dp[0] = a[0]
    for i in range(1, n):
        dp[i][0] = a[i][0] + max(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = a[i][1] + max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = a[i][2] + max(dp[i - 1][0], dp[i - 1][1])
    print(max(dp[n - 1]))


if __name__ == "__main__":
    main()
