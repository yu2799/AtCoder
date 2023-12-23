from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [1, 1]
    MOD = 998244353
    for i in range(1, n):
        _dp = [0, 0]
        if ab[i - 1][0] != ab[i][0]:
            _dp[0] += dp[0]
        if ab[i - 1][1] != ab[i][0]:
            _dp[0] += dp[1]
        if ab[i - 1][0] != ab[i][1]:
            _dp[1] += dp[0]
        if ab[i - 1][1] != ab[i][1]:
            _dp[1] += dp[1]
        dp[0] = _dp[0] % MOD
        dp[1] = _dp[1] % MOD
    print(sum(dp) % MOD)


if __name__ == "__main__":
    main()
