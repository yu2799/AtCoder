from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print((a + b - 1) // b)


if __name__ == "__main__":
    main()
