from sys import stdin


def main():
    input = stdin.readline
    n, a, x, y = map(int, input().split())
    print(min(n, a) * x + max(0, n - a) * y)


if __name__ == "__main__":
    main()
