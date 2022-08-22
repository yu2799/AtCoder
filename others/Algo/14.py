from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    if n == 1:
        print(1)
    else:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        print(dp[-1])


if __name__ == "__main__":
    main()
