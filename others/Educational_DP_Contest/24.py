from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    dp = [[0] * n for _ in [0] * n]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            if i - 1 > -1:
                dp[i][j] += dp[i - 1][j]
            if j - 1 > -1:
                dp[i][j] += dp[i][j - 1]
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
