from sys import stdin


def main():
    input = stdin.readline
    n, x, t = map(int, input().split())
    print(((n + x - 1) // x) * t)


if __name__ == "__main__":
    main()
