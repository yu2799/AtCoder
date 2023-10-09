from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = input()[:-1]
    dp = [0] * 7
    MOD = 10**9 + 7
    buf = {
        "a": 0,
        "t": 1,
        "c": 2,
        "o": 3,
        "d": 4,
        "e": 5,
        "r": 6,
    }
    for i in s:
        if i == "a":
            dp[0] += 1
        elif i in buf:
            dp[buf[i]] += dp[buf[i] - 1] % MOD
    print(dp[-1] % MOD)


if __name__ == "__main__":
    main()
