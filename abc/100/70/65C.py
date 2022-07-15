from sys import stdin


def main():
    input = stdin.readline
    n, m = sorted(map(int, input().split()))
    MOD = 10**9 + 7
    if m - n <= 1:
        res = 1
        for i in range(2, n + 1):
            res = res * i % MOD
        res = pow(res, 2, MOD)
        print(res * (2 if m == n else m) % MOD)
    else:
        print(0)


if __name__ == "__main__":
    main()
