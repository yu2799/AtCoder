from sys import stdin


def main():
    input = stdin.readline
    a = [int(i) for i in input().split()]
    dp = [[0] * 4 for _ in [0] * 4]
    dp[0] = a
    for i in range(1, 4):
        for j in range(4):
            dp[i][j] += dp[i - 1][j]
            if j - 1 >= 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j - 1 < 4:
                dp[i][j] += dp[i - 1][j + 1]
    print(dp[3][3])


if __name__ == "__main__":
    main()
