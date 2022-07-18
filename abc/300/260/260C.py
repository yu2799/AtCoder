from sys import stdin


def red(n, x, y):
    if n == 1:
        return 0
    return red(n - 1, x, y) + blue(n, x, y) * x


def blue(n, x, y):
    if n == 1:
        return 1
    return red(n - 1, x, y) + blue(n - 1, x, y) * y


def main():
    input = stdin.readline
    n, x, y = map(int, input().split())
    print(red(n, x, y))


if __name__ == "__main__":
    main()
