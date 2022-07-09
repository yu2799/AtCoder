from sys import stdin


def ncr(n, r, mod):
    ret = 1
    for i in range(1, r + 1):
        ret = (ret * (n - i + 1) * pow(i, mod - 2, mod)) % mod
    return ret


def main():
    input = stdin.readline
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    print((pow(2, n, MOD) - ncr(n, a, MOD) - ncr(n, b, MOD) - 1) % MOD)


if __name__ == "__main__":
    main()
