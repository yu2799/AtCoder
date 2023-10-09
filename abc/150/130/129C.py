from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = set(int(input()) for _ in range(m))
    dp = [0] * (n + 1)
    dp[0] = 1
    MOD = 10**9 + 7
    for i in range(n):
        if i + 1 <= n and i + 1 not in a:
            dp[i + 1] += dp[i]
            dp[i + 1] %= MOD
        if i + 2 <= n and i + 2 not in a:
            dp[i + 2] += dp[i]
            dp[i + 2] %= MOD
    print(dp[-1])


if __name__ == "__main__":
    main()
