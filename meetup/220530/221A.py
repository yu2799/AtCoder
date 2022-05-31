from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print(32 ** (a - b))


if __name__ == "__main__":
    main()
