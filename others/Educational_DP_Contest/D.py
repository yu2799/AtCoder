from sys import stdin


def main():
    input = stdin.readline
    n, w = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in [0] * n]
    dp = [[0] * (w + 1) for _ in [0] * (n + 1)]
    for i in range(n):
        weight, value = wv[i]
        for j in range(w + 1):
            if j + weight < w + 1:
                dp[i + 1][j + weight] = max(
                    dp[i + 1][j + weight], dp[i][j] + value
                )
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    print(dp[n][w])


if __name__ == "__main__":
    main()
