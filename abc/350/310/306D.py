from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    dp = [0, 0]
    for _ in range(n):
        x, y = map(int, input().split())
        tmp = [0, 0]
        if x == 0:
            tmp[0] = max(dp[0] + y, dp[1] + y, dp[0])
            tmp[1] = dp[1]
        else:
            tmp[0] = dp[0]
            tmp[1] = max(dp[0] + y, dp[1])
        dp = tmp
    print(max(dp))


if __name__ == "__main__":
    main()
