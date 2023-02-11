from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = set(int(input()) for _ in range(m))
    dp = [0] * (n + 1)
    dp[0] = 1
    MOD = 10**9 + 7
    for i in range(n + 1):
        if i in a:
            continue
        if i < n:
            dp[i + 1] += dp[i]
        if i + 1 < n:
            dp[i + 2] += dp[i]
        dp[i] %= MOD
    print(dp[-1])


if __name__ == "__main__":
    main()
