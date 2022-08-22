from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    d = [int(i) for i in input().split()]
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in d:
            if i - j >= 0 and dp[i - j]:
                dp[i] = True
                break
    print("Yes" if dp[-1] else "No")


if __name__ == "__main__":
    main()
