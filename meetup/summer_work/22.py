from sys import stdin


def main():
    input = stdin.readline
    n, w = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [-1] * (w + 1)
    dp[0] = 0
    res = 0
    for i in range(n):
        _dp = dp[:]
        weight, value = wv[i]
        for j in range(w):
            if weight + j > w:
                break
            if dp[j] == -1:
                continue
            _dp[j] = max(dp[j], _dp[j])
            _dp[weight + j] = max(dp[weight + j], dp[j] + value)
        dp = _dp
        res = max(res, max(dp))
    print(res)


if __name__ == "__main__":
    main()
