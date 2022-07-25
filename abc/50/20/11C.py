from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    ng = {int(input()) for _ in [0] * 3}
    dp = [[False] * (n + 1) for _ in [0] * 101]
    dp[0][0] = True
    for i in range(1, 101):
        for j in range(n + 1):
            if j in ng:
                continue
            for k in range(1, 4):
                if j - k >= 0 and dp[i - 1][j - k]:
                    dp[i][j] = True
        if dp[i][n]:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    main()
