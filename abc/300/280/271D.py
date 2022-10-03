from sys import stdin


def main():
    input = stdin.readline
    n, s = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in [0] * n]
    dp = [["-1"] * (s + 1) for _ in [0] * (n + 1)]
    dp[0][0] = ""

    for i in range(n):
        for j in range(s):
            if dp[i][j] != "-1":
                a, b = ab[i]
                if j + a <= s:
                    dp[i + 1][j + a] = dp[i][j] + "H"
                if j + b <= s:
                    dp[i + 1][j + b] = dp[i][j] + "T"

    if dp[-1][-1] != "-1":
        print("Yes")
        print(dp[-1][-1])
    else:
        print("No")


if __name__ == "__main__":
    main()
