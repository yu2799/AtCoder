from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    t = input()[:-1]
    s_len = len(s)
    t_len = len(t)
    dp = [[0] * (t_len + 1) for _ in [0] * (s_len + 1)]
    for i in range(s_len):
        for j in range(t_len):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    res = ""
    cnt = dp[-1][-1]
    i = s_len
    j = t_len
    while cnt > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            i -= 1
            j -= 1
            cnt -= 1
            res = t[j] + res

    print(res)


if __name__ == "__main__":
    main()
