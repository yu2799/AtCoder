from sys import stdin


def main():
    input = stdin.readline
    n, d = map(int, input().split())
    print((n + (d * 2 + 1) - 1) // (d * 2 + 1))


if __name__ == "__main__":
    main()
