from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [[int(i) for i in input().split()] for _ in [0] * n]
    dp = [[0] * n for _ in [0] * n]
    dp[0][0] = a[0][0]
    for i in range(n):
        for j in range(n):
            if i - 1 > -1:
                dp[i][j] = dp[i - 1][j] + a[i][j]
            if j - 1 > -1:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + a[i][j])
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
