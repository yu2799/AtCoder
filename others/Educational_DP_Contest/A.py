from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    h = [int(i) for i in input().split()]

    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(h[1] - h[0])
    for i in range(2, n):
        a = dp[i - 2] + abs(h[i] - h[i - 2])
        b = dp[i - 1] + abs(h[i] - h[i - 1])
        if a < b:
            dp[i] = a
        else:
            dp[i] = b
    print(dp[-1])


if __name__ == "__main__":
    main()
