from collections import defaultdict
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    xd = defaultdict(int)
    ad = defaultdict(int)
    for _ in [0] * n:
        t, x, a = map(int, input().split())
        xd[t] = x + 1
        ad[t] = a
        t_max = t + 1

    dp = [[0] * 5 for _ in [0] * t_max]
    for i in range(t_max - 1):
        dp[i + 1][0] = max(dp[i][0], dp[i][1]) + (
            ad[i + 1] if xd[i + 1] == 1 else 0
        )
        dp[i + 1][1] = max(dp[i][0], dp[i][1], dp[i][2]) + (
            ad[i + 1] if xd[i + 1] == 2 else 0
        )
        dp[i + 1][2] = max(dp[i][1], dp[i][2], dp[i][3]) + (
            ad[i + 1] if xd[i + 1] == 3 and i >= 1 else 0
        )
        dp[i + 1][3] = max(dp[i][2], dp[i][3], dp[i][4]) + (
            ad[i + 1] if xd[i + 1] == 4 and i >= 2 else 0
        )
        dp[i + 1][4] = max(dp[i][3], dp[i][4]) + (
            ad[i + 1] if xd[i + 1] == 5 and i >= 3 else 0
        )

    print(max(dp[-1]))


if __name__ == "__main__":
    main()
