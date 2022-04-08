from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    dp = [0] * n
    dp[0] = 0
    for i in range(1, n):
        tmp = []
        for j in range(1, m + 1):
            if i - j >= 0:
                tmp.append(dp[i - j] + a[i] * j)
        dp[i] = min(tmp)
    print(dp[-1])


if __name__ == "__main__":
    main()
