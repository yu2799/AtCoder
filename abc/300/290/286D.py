from sys import stdin


def main():
    input = stdin.readline
    n, x = map(int, input().split())
    dp = [False] * (x + 1)
    dp[0] = True
    for _ in [0] * n:
        a, b = map(int, input().split())
        tmp = []
        for i in range(x + 1):
            if dp[i]:
                tmp.append(i)
        for i in tmp:
            for j in range(1, b + 1):
                if i + a * j <= x:
                    dp[i + a * j] = True
    print("Yes" if dp[-1] else "No")


if __name__ == "__main__":
    main()
