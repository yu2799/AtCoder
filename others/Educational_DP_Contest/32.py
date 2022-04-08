from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    dp = [[False] * (m + 1) for _ in [0] * (n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for j in range(m + 1):
            if dp[i - 1][j]:
                dp[i][j] = True
            if j - w[i - 1] > -1 and dp[i - 1][j - w[i - 1]]:
                dp[i][j] = True
    print("Yes" if dp[-1][-1] else "No")


if __name__ == "__main__":
    main()
