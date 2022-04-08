from sys import stdin


def main():
    input = stdin.readline
    N, W = map(int, input().split())
    w = []
    v = []
    dp = [[0] * (W + 1) for _ in [0] * (N + 1)]
    for _ in [0] * N:
        a, b = map(int, input().split())
        w.append(a)
        v.append(b)

    for i in range(N):
        # 品物をi個選んだとき
        for j in range(W + 1):
            # 重さがj以下のとき
            if j >= w[i]:
                dp[i + 1][j] = max(dp[i][j - w[i]] + v[i], dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][-1])


if __name__ == "__main__":
    main()
