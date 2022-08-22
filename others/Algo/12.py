from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    dp = [0] * n
    dp[0] = 0
    for i in range(1, n):
        dp[i] = min(a[i] + dp[i - 1], a[i] * 2 + dp[i - 2])
    print(dp[-1])


if __name__ == "__main__":
    main()
