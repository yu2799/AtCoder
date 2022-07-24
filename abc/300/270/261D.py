from sys import stdin
from collections import defaultdict


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    d = defaultdict(int)
    for _ in [0] * m:
        c, y = map(int, input().split())
        d[c] = y
    dp = [[0] * (n + 1) for _ in [0] * (n + 1)]
    prev = 0
    for i in range(1, n + 1):
        dp[i][0] = prev
        for j in range(1, i + 1):
            tmp = dp[i - 1][j - 1] + x[i - 1] + d[j]
            dp[i][j] = tmp
            if prev < tmp:
                prev = tmp
    print(prev)


if __name__ == "__main__":
    main()
