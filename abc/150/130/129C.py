from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = set([int(input()) for _ in [0] * m])
    mod = 10 ** 9 + 7
    dp = [0] * (n + 2)
    dp[0] = 1
    for i in range(1, n + 1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    print(dp[n])


if __name__ == "__main__":
    main()
