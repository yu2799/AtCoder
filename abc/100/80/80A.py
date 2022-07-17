from sys import stdin


def main():
    input = stdin.readline
    n, a, b = map(int, input().split())
    print(a * n if (a * n) < b else b)


if __name__ == "__main__":
    main()
