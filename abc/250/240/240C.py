from sys import stdin


def main():
    input = stdin.readline
    n, x = map(int, input().split())
    dp = [[False] * (x + 1) for _ in [0] * (n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        for j in range(1, x + 1):
            if j - a > -1 and dp[i - 1][j - a]:
                dp[i][j] = True
            elif j - b > -1 and dp[i - 1][j - b]:
                dp[i][j] = True
    print("Yes" if dp[n][x] else "No")


if __name__ == "__main__":
    main()
