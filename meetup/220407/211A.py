from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print((a + 2 * b) / 3)


if __name__ == "__main__":
    main()
