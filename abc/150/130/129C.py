from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = set(int(input()) for _ in [0] * m)
    dp = [0] * (n + 1)
    dp[0] = 1
    MOD = 10**9 + 7
    for i in range(1, n + 1):
        if i not in a:
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    print(dp[n])


if __name__ == "__main__":
    main()
