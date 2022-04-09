from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    MOD = 998244353
    print((a * (a+1)//2) % MOD * (b * (b+1)//2) % MOD * (c * (c+1)//2) % MOD)


if __name__ == '__main__':
    main()
