from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    MOD = 998244353
    dp = [1] * 3001
    for i in range(n):
        tmp = [0] * 3001
        for j in range(a[i], b[i] + 1):
            tmp[j] = dp[j]
        dp = tmp
        for i in range(3000):
            dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
    print(dp[3000])


if __name__ == "__main__":
    main()
