from sys import stdin


def main():
    input = stdin.readline
    n, i = map(int, input().split())
    print(n - i + 1)


if __name__ == "__main__":
    main()
