from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    t = list(map(int, input().split()))
    max_t = sum(t) + 1
    dp = [False] * max_t
    dp[0] = True

    for c in t:
        dp_ = dp[:]
        for i in range(max_t - 1, -1, -1):
            if dp_[i] and i + c < max_t:
                dp[i + c] = True
            dp[i] = dp_[i]

    for i in range(max_t // 2, max_t + 1):
        if dp[i]:
            print(i)
            return


if __name__ == "__main__":
    main()
