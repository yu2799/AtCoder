from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    grid = (
        [list("#" * (w + 2))]
        + [list("#") + list(input()[:-1]) + list("#") for _ in [0] * h]
        + [list("#" * (w + 2))]
    )
    MOD = 10**9 + 7
    dp = [[0] * (w + 2) for _ in [0] * (h + 2)]
    dp[1][1] = 1
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if grid[i + 1][j] == ".":
                dp[i + 1][j] += dp[i][j] % MOD
            if grid[i][j + 1] == ".":
                dp[i][j + 1] += dp[i][j] % MOD
    print(dp[h][w] % MOD)


if __name__ == "__main__":
    main()
