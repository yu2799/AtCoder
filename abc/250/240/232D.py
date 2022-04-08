from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    c = [input()[:-1] for _ in [0] * h]
    dp = [[0] * w for _ in [0] * h]
    dp[0][0] = 1
    res = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == "#":
                continue
            if i - 1 > -1 and dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j] + 1
            if j - 1 > -1 and dp[i][j - 1]:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)
        tmp = max(dp[i])
        if tmp > res:
            res = tmp
    print(res)


if __name__ == "__main__":
    main()
