from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    print((6 * (k - 1) * (n - k) + 3 * (n - 1) + 1) / (n**3))


if __name__ == "__main__":
    main()
