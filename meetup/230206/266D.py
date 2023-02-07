from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    d = {}
    max_t = 0
    for _ in range(n):
        t, x, a = map(int, input().split())
        d[t] = (x, a)
        max_t = t
    dp = [[0] * 5 for _ in range(max_t + 1)]
    for i in range(max_t):
        for j in range(5):
            tmp = 0
            for k in range(-1, 2):
                if 0 <= j + k <= 4:
                    tmp = max(tmp, dp[i][j + k])
            dp[i + 1][j] = tmp + (
                d[i + 1][1]
                if i + 1 >= j and i + 1 in d and d[i + 1][0] == j
                else 0
            )
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
