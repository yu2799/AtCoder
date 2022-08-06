from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    MOD = 10**9 + 7
    print((a * b % MOD) * c % MOD)


if __name__ == "__main__":
    main()
