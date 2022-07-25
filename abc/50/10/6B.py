from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    dp = [0] * n
    if n <= 2:
        print(0)
        return
    dp[2] = 1
    for i in range(3, n):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 10007
    print(dp[n - 1])


if __name__ == "__main__":
    main()
