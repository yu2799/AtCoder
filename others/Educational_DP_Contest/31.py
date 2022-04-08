from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[False] * m for _ in [0] * n]
    dp[0][0] = True
    for i in range(1, n):
        for j in range(m):
            if i - 1 > -1 and dp[i - 1][j]:
                dp[i][j] = True
            if j - a[i - 1] > -1 and dp[i - 1][j - a[i - 1]]:
                dp[i][j] = True
    print(sum(dp[-1]))


if __name__ == "__main__":
    main()
