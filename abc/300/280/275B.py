from sys import stdin


def main():
    input = stdin.readline
    a, b, c, d, e, f = map(int, input().split())
    MOD = 998244353
    print(((a * b * c) - (d * e * f)) % MOD)


if __name__ == "__main__":
    main()
