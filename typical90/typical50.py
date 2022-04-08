from sys import stdin
from math import comb


def main():
    input = stdin.readline
    n, l = map(int, input().split())
    mod = 10 ** 9 + 7
    """
    combination
    """
    # res = 0
    # cnt = n // l
    # for i in range(cnt+1):
    #     res += comb(n + i * (1-l), i) % mod
    # print(res % mod)
    """
    dp漸化式
    """
    dp = [1] * (n + 1)
    for i in range(l, n+1):
        dp[i] = (dp[i - 1] + dp[i - l]) % mod
    print(dp[n])


if __name__ == '__main__':
    main()
