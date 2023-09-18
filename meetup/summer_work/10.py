from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    abc = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [0, 0, 0]
    for i in range(n):
        tmp = dp[:]
        tmp[0] = max(dp[1] + abc[i][0], dp[2] + abc[i][0])
        tmp[1] = max(dp[0] + abc[i][1], dp[2] + abc[i][1])
        tmp[2] = max(dp[0] + abc[i][2], dp[1] + abc[i][2])
        dp = tmp
    print(max(dp))


if __name__ == "__main__":
    main()
