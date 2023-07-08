from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = 1
    MOD = 10**9 + 7
    for i in range(1, n + 1):
        res = res * i % MOD
    print(res)


if __name__ == "__main__":
    main()
