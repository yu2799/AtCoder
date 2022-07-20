from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    MOD = 10**9 + 7
    print((n - k + 2) * (n * n + n * k - 2 * k * k + n + 2 * k + 6) // 6 % MOD)


if __name__ == "__main__":
    main()
