from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    if n == 1:
        print(k)
    else:
        print(k * (k - 1) % mod * pow(k-2, n-2, mod) % mod)


if __name__ == '__main__':
    main()
