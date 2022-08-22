from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    dp = [[0] * 3 for _ in [0] * (n + 1)]
    for i in range(n):
        a, b, c = map(int, input().split())
        dp[i + 1][0] = max(dp[i][1], dp[i][2]) + a
        dp[i + 1][1] = max(dp[i][2], dp[i][0]) + b
        dp[i + 1][2] = max(dp[i][0], dp[i][1]) + c
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
