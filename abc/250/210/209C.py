from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    MOD = 10**9 + 7
    res = 1
    for i in range(n):
        res = res * max(0, c[i] - i) % MOD
    print(res)


if __name__ == "__main__":
    main()
