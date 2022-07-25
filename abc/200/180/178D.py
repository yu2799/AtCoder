from sys import stdin


def main():
    input = stdin.readline
    s = int(input())
    MOD = 10**9 + 7
    dp = [0] * (s + 1)
    dp[0] = 1
    for i in range(1, s + 1):
        for j in range(i - 2):
            dp[i] += dp[j]
        dp[i] %= MOD
    print(dp[s])


if __name__ == "__main__":
    main()
