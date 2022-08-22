from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    h = list(map(int, input().split()))
    INF = float("inf")
    dp = [INF] * n
    dp[0] = 0
    for i in range(n):
        if i + 2 < n:
            dp[i + 2] = min(dp[i + 2], abs(h[i + 2] - h[i]) + dp[i])
        if i + 1 < n:
            dp[i + 1] = min(dp[i + 1], abs(h[i + 1] - h[i]) + dp[i])
    print(dp[n - 1])


if __name__ == "__main__":
    main()
