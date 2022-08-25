from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    INF = 10**9
    dp = [INF] * n
    dp[0] = 0

    for i in range(n):
        if i + 2 < n:
            dp[i + 2] = min(dp[i + 2], abs(a[i] - a[i + 2]) + dp[i])
        if i + 1 < n:
            dp[i + 1] = min(dp[i + 1], abs(a[i] - a[i + 1]) + dp[i])
    print(dp[-1])


if __name__ == "__main__":
    main()
