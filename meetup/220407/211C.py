from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    l = len(s)
    dp = [[0] * 9 for _ in [0] * (l + 1)]
    t = "chokudai"
    MOD = 10 ** 9 + 7
    for i in range(l + 1):
        dp[i][0] = 1
    for i in range(1, l + 1):
        for j in range(1, 9):
            if s[i - 1] != t[j - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
