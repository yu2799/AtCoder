from sys import stdin


def main():
    input = stdin.readline
    n, x, y = map(int, input().split())
    dp = [0] * n
    dp[0] = x
    dp[1] = y
    for i in range(2, n):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 100
    print(dp[-1])


if __name__ == "__main__":
    main()
