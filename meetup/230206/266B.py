from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    MOD = 998244353
    print(n % MOD)


if __name__ == "__main__":
    main()
