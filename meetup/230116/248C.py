from sys import stdin


def main():
    input = stdin.readline
    n, m, k = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (k + 1) for _ in [0] * (n + 1)]
    dp[0][0] = 1
    for a in range(n):
        for b in range(k):
            for c in range(1, m + 1):
                if b + c <= k:
                    dp[a + 1][b + c] += dp[a][b]
                    dp[a + 1][b + c] %= MOD
    res = 0
    for i in range(1, k + 1):
        res += dp[n][i]
        res %= MOD
    print(res)


if __name__ == "__main__":
    main()
