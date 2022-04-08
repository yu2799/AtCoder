from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    mod = 10 ** 9 + 7
    print((pow(10, n, mod) - 2 * pow(9, n, mod) + pow(8, n, mod)) % mod)


if __name__ == "__main__":
    main()
