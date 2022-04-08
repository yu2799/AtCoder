from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    h = [int(i) for i in input().split()]

    dp = [0] * n
    dp[0] = 0
    for i in range(1, n):
        tmp = []
        for j in range(max(0, i - k), i):
            tmp.append(abs(h[j] - h[i]) + dp[j])
        dp[i] = min(tmp)
    print(dp[-1])


if __name__ == "__main__":
    main()
