from sys import stdin


def main():
    input = stdin.readline
    n, m, _ = map(int, input().split())
    abc = [tuple(map(int, input().split())) for _ in [0] * m]
    e = map(int, input().split())
    INF = 10**18
    dp = [INF] * n
    dp[0] = 0

    for i in e:
        a, b, c = abc[i - 1]
        a -= 1
        b -= 1
        tmp = dp[a] + c
        if tmp < dp[b]:
            dp[b] = tmp
    print(dp[-1] if dp[-1] != INF else -1)


if __name__ == "__main__":
    main()
