from sys import stdin


def main():
    input = stdin.readline
    h, a = map(int, input().split())
    print((h + a - 1) // a)


if __name__ == "__main__":
    main()
