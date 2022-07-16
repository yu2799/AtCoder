from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    print((1900 * m + 100 * (n - m)) * pow(2, m))


if __name__ == "__main__":
    main()
