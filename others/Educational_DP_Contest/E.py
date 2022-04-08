from sys import stdin


def main():
    input = stdin.readline
    N, W = map(int, input().split())
    w = []
    v = []
    for _ in [0] * N:
        a, b = map(int, input().split())
        w.append(a)
        v.append(b)
    INF = 10 ** 15
    maxV = sum(v) + 1
    dp = [[INF] * maxV for _ in [0] * (N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(maxV):
            if j >= v[i]:
                dp[i + 1][j] = min(dp[i][j - v[i]] + w[i], dp[i][j])
            else:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    res = 0
    for i in range(maxV):
        if dp[N][i] <= W:
            res = i
    print(res)


if __name__ == "__main__":
    main()
