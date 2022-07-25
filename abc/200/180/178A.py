from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    print((x + 1) % 2)


if __name__ == "__main__":
    main()
