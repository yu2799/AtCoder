from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    mod = 998244353
    l = len(str(n))
    tmp = 0
    res = 0
    for i in range(l - 1):
        a = 9 * 10 ** i
        tmp += a
        res += a * (a + 1) // 2 % mod
    res += (n - tmp) * (n - tmp + 1) // 2 % mod
    print(res % mod)


if __name__ == "__main__":
    main()
